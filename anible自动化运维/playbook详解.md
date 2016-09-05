#####playbook基本语法；

* YAML 基本语法；
    - [Ansible 中文指南](http://ansible-tran.readthedocs.io/en/latest/docs/YAMLSyntax.html)
    - [www.yaml.org](http://www.yaml.org/spec/1.2/spec.html)
```
---
- hosts: localhost
  tasks:
    - name: Install Nginx Package
      yum: name=nginx state=present

    - name: Copy Nginx.conf
      template: src=./nginx.conf.j2 dest=/etc/nginx/nginx.conf owner=root mode=0644 validate='nnginx -t -c %s'
      notify:
        - ReStart Nginx Service

  handlers:
    - name: ReStart Nginx Service
      service: name=nginx state=restarted

```



假装今天有更新github