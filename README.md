# Odoo Password Hasher

In case you need to recover your password, for development/testing environment, or else, this may help.

## How to install

1. Clone this repo to you addon path.
```
$ git clone https://github.com/azhargiri/odoo-password-hasher /path/to/odoo-addons/password_hasher
```

2. Execute as odoo command. May be different depending on how you setup the application.
```
$ python odoo-bin hasher halo
```
It will produce something like
```
$pbkdf2-sha512$25000$K6XU.j8nZMx5L8X4/39vDQ$zL2gp9nZmsfwLxxAVbjg9.ks0NClUIxn0MvMpa/iTBjSNnAa8BPvgF8cv.Agcw7fzYeJ.a.GZvuSiIB20m4EpA
```

3. Update `password` column table `res_users`. Use your favorite database editor or invoke SQL `update` command.
