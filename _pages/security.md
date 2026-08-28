---
layout: page
permalink: /security/
title: digital ID
description: Public X.509 certificates for verifying signed documents and S/MIME email.
nav: true
nav_order: 9
---

Use the public X.509 certificates below to verify documents or S/MIME email signed by me. Download a certificate and compare its SHA-256 fingerprint with the value shown here.

## Personal identity

- **Name:** Santiago Casas
- **Email:** `s.casas@protonmail.com`
- **Certificate:** [my_signature.crt](/assets/keys/my_signature.crt)
- **SHA-256 fingerprint:** `9E:C6:18:46:CC:66:13:28:05:3F:4C:23:18:73:5E:19:EE:42:EE:D6:99:AC:C1:11:1D:46:42:1F:4A:5B:28:63`

## RWTH Aachen identity

- **Name:** Santiago Casas
- **Email:** `casas@physik.rwth-aachen.de`
- **Certificate:** [rwth_signature.crt](/assets/keys/rwth_signature.crt)
- **SHA-256 fingerprint:** `1B:15:A3:28:C5:64:74:46:4D:21:E1:86:12:24:A5:2D:2C:07:FD:17:4F:D5:FE:A0:AD:93:3D:7F:31:21:88:6A`

## Verification

In your email client or document viewer, compare the certificate's SHA-256 fingerprint with the matching value above. A matching fingerprint confirms that the certificate is the one published on this website.

> These certificates are self-signed. Their validity is established by verifying the published fingerprint through this HTTPS site, not by a public certificate authority.
