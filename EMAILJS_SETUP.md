# EmailJS Contact Form Setup Guide

This guide will help you set up the contact form on your portfolio to send emails using EmailJS.

## Step 1: Create EmailJS Account

1. Go to [EmailJS](https://www.emailjs.com/)
2. Click "Sign Up" and create a free account
3. Verify your email address

## Step 2: Add Email Service

1. In your EmailJS dashboard, go to "Email Services"
2. Click "Add New Service"
3. Choose your email provider (Gmail, Outlook, Yahoo, etc.)
4. Connect your email account and give it a name (e.g., "Portfolio Contact")
5. Note down the **Service ID** (something like `service_xxxxx`)

## Step 3: Create Email Template

1. Go to "Email Templates" in your dashboard
2. Click "Create New Template"
3. Set up the template:

**To Email:** `mudash254@gmail.com` (your email)

**From Name:** `{{from_name}}`

**From Email:** `{{from_email}}`

**Subject:** `New Contact Form Message from {{from_name}}`

**Message Body:**
```
Hi Daniel,

You have received a new message from your portfolio contact form:

Name: {{from_name}}
Email: {{from_email}}

Message:
{{message}}

Best regards,
Portfolio Contact Form
```

4. Save the template and note down the **Template ID** (something like `template_xxxxx`)

## Step 4: Get Your Public Key

1. Go to "Account" in your dashboard
2. Copy your **Public Key** (something like `xxxxxxxxxxxxxx`)

## Step 5: Update Your Portfolio Code

Update `index.html` with your EmailJS credentials:

1. Replace `your_public_key_here` with your Public Key
2. Replace `your_service_id_here` with your Service ID
3. Replace `your_template_id_here` with your Template ID

## Step 6: Test the Form

1. Deploy your changes to GitHub Pages
2. Visit your portfolio and fill out the contact form
3. Submit it and check your email for the message

## Troubleshooting

- **Emails not sending?** Check your EmailJS dashboard for error logs
- **Service not working?** Make sure your email service is properly connected
- **Template issues?** Verify the variable names match exactly (`{{from_name}}`, etc.)

## Security Note

EmailJS sends emails from your browser using their service. Your email credentials are stored securely on EmailJS servers, not in your code.

For more help, visit the [EmailJS Documentation](https://www.emailjs.com/docs/).