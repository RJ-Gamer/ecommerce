"""
Email Thread to send many emails at once
"""
import logging
from concurrent.futures import ThreadPoolExecutor

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _
from rest_framework.serializers import ValidationError

from shared.utils import messages


log = logging.getLogger(__name__)


class EmailThread:
    """
    Email Thread to send many emails at once
    """

    def __init__(
        self,
        subject: str,
        body=None,
        from_email=None,
        template_name=None,
        context=None,
        attachments=None,
    ):
        """
        initialize email thread
        """
        self.subject = subject
        self.body = body
        self.from_email = from_email
        self.template_name = template_name
        self.context = context
        self.attachments = attachments

    def send_one_email(self, to_email: str):
        """
        Sends the same email to a single recipient using EmailMultiAlternatives.

        Args:
            to_email (str): The email address to send the email to.
        """
        if self.template_name:
            html_content = render_to_string(self.template_name, self.context)
        else:
            html_content = self.body

        email = EmailMultiAlternatives(
            subject=self.subject,
            body=html_content,
            from_email=self.from_email,
            to=[to_email],
        )
        email.attach_alternative(html_content, "text/html")
        if self.attachments:
            for attachment in self.attachments:
                email.attach_file(attachment)
        try:
            email.send()
            log.info(messages.LOG_EMAIL_SENT.format(to_email))
            return True
        except Exception as error:
            log.error(messages.LOG_EMAIL_NOT_SENT.format(to_email, error))
            return False

    def send_emails(self, receiver_list: list[str] = None, num_threads: int = 10):
        """
        Sends the same email to multiple recipients in parallel using a thread pool.

        Args:
            to_emails (List[str]): A list of email addresses to send the email to.
            num_threads (int): The number of threads to use for sending emails in parallel.

        Returns:
            A tuple containing the number of successful emails and the number of failed emails.
        """
        if receiver_list is None or len(receiver_list) == 0:
            raise ValidationError({"message": _(messages.ERR_NO_RECEIVER)})

        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            yield [
                executor.submit(self.send_one_email, email) for email in receiver_list
            ]
