from main import send_email, ContactForm
from unittest.mock import patch

@patch("smtplib.SMTP")
def test_send_email(mock_smtp):
    """Test the send_email function using a mocked SMTP server."""
    mock_smtp_instance = mock_smtp.return_value
    mock_smtp_instance.starttls.return_value = None
    mock_smtp_instance.login.return_value = None
    mock_smtp_instance.sendmail.return_value = None

    # Create a ContactForm object if required
    contact_form = ContactForm(
        name="Test Name",
        email="test@example.com",
        phone="1234567890",
        title="Test Title",
        message="Test Message"
    )

    # Call the function
    response = send_email(contact_form)  # Pass the ContactForm object

    # Verify the function completed successfully
    assert response == {"message": "Email sent"}
    mock_smtp_instance.sendmail.assert_called_once()
