# OpenSSL

## RSA

$ openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:4096 -aes-256-cbc -out private.key

Generates a 4096-bit RSA encryption key secured with a password phrase you need to enter.

### certificate

$ openssl req -new -out certificate.csr -key private.key

To generate a certificate file.
