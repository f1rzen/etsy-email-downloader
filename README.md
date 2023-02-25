# etsy-email-downloader
a script written in python using playwright to download customer emails from etsy sales.

This script uses playwright and semicolon seperated csv.

# Usage
change the line 11 with your etsy user name

change the line 13 with your etsy password

change the line 19 with your page number +1  when order number per page selected 50 order per page.

for example:

![example etsy page](https://black_hole-3kf-1-c9822425.deta.app/api/photo/2b506u8a5xdb.png)

99+1 = 100

in this stiuation our line 19 is gonna be like this:

```
for j in range(0,100):
```




*install* the playwright

```
pip install playwright
```

*run* the script

```
python ./app.py
```

# TroubleShooting

If scripts breaks, uncomment the line 16 and change the x with your last page number and change the zero with your last page number in line 19



