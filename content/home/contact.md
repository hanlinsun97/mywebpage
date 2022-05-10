---
# An instance of the Contact widget.
widget: contact

# This file represents a page section.
headless: true

# Order that this section appears on the page.
weight: 130

title: Contact
subtitle:

content:
  # Automatically link email and phone or display as text?
  autolink: true

  # Email form provider
  form:
    provider: netlify
    formspree:
      id:
    netlify:
      # Enable CAPTCHA challenge to reduce spam?
      captcha: false

  # Contact details (edit or remove options as required)
  email: hanlin.sun@qmul.ac.uk
  address:
    street: Mile End Road
    city: London
    postcode: 'E1 4NS'
    country: United Kingdom
    country_code: UK
  coordinates:
    latitude: '51.522538381861125'
    longitude: '-0.04305267040285758'
  directions: Math Building MB-402
  
  contact_links:
    - icon: twitter
      icon_pack: fab
      name: DM Me
      link: 'https://twitter.com/sunhanlin151'

design:
  columns: '2'
---
