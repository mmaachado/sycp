WAF - Web Application Firewall
IDS - Intrusion Detection System
IPS - Intrusion Prevention System

wafw00f <url>

nmap -p 80,443 <url> --script=http-waf-detect - simula envios de requisições maliciosas para detectar IPS/IDS

nmap -p 80,443 <url> --script=http-waf-fingerprint - analisa as respostas das requisições para identificar fingerprints