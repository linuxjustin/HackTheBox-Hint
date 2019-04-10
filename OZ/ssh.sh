for x in 40809 50212 46969; do nmap -sU -Pn --host-timeout 201 --max-retries 0 -p $x 10.10.10.96; done

ssh dorthi@10.10.10.96 -i id_rsa
