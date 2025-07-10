
> curl -I https://trudeau.dev/helloworld.html
> curl -v --include https://trudeau.dev/helloworld.html

## HTTPS

+ HTTPS both encrypts traffic and offers verification of site identity
+ Authentication
  + PKI: Public Key Infrastructure
  + Certificates identify sites
    + Issued TO: who ownes the certificate
    + Issued by: who issued the certificate
    + Validity Period: time frame within which certificate is valid

> https://hackernoon.com/how-does-rsa-work-f44918df914b

> lsof -i @localhost
> nmap -A -p T:5600-5700 localhost
