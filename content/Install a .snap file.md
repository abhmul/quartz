---

title: "Install a .snap file"

---
See [this askubuntu answer](https://askubuntu.com/questions/1266894/how-can-i-install-a-snap-package-from-a-local-file). Basically the command is 
```bash
snap install ./abc.snap --dangerous
```

You can put a `sudo` in front if you need admin privelages. The `--dangerous` skips the signature verification.