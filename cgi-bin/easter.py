#!/usr/bin/python3
import cgi , cgitb
cgitb.enable()
form = cgi.FieldStorage() 
year = int(form.getvalue('theYear'))
date_format = form.getvalue('dateformat')


def Easter(y): 
   a = y % 19   
   b = y // 100   
   c = y % 100   
   d = b // 4   
   e = b % 4   
   g = (8 * b + 13) // 25   
   h = (19 * a + b - d - g + 15) % 30   
   j = c // 4 
   k = c % 4 
   m = (a + 11 * h) // 319 
   r = (2 * e + 2 * j - k - h + m + 32) % 7 
   n = (h - m + r + 90) // 25 
   p = (h - m + r + n + 19) % 32 
  
   if len(str(p))==1:
    date=str((f"<b>0{p}/0{n}/{y}</b>"))

   else:
    date=str((f"<b>{p}/0{n}/{y}</b>"))
   return date

def EasterV2(y): 
   a = y % 19   
   b = y // 100   
   c = y % 100   
   d = b // 4   
   e = b % 4   
   g = (8 * b + 13) // 25   
   h = (19 * a + b - d - g + 15) % 30   
   j = c // 4 
   k = c % 4 
   m = (a + 11 * h) // 319 
   r = (2 * e + 2 * j - k - h + m + 32) % 7 
   n = (h - m + r + 90) // 25 
   p = (h - m + r + n + 19) % 32 

   days ={
     (1,21,31): "st",
     (2,22): "nd",
     (3,23): "rd"
   }#if date of the month is any of the above number, the date ending changes

   months={
     3: "March",
     4: "April",
   }
  
   default="th"

   for key, day in days.items():
     if p in key: #if the day is in the above dictionary the ending becomes st, nd, or rd
       ending = day
       break
     else:
       ending = default #if the day isn't above it becomes th

   month=months.get(n)

   date=str((f"<b>{p}<sup>{ending}</sup> {month} {y}</b>"))
   return date


if date_format == "ddmmyyyy-":
    thedate=(Easter(year))
elif date_format == "daymonthyear-":
    thedate=(EasterV2(year))
elif date_format == "bothdates-":
    thedate=(f"<b>{Easter(year)}</b> or <b>{EasterV2(year)}</b>")

else:
    thedate="Didn't work"

print('Content-Type: text/html; charset=utf-8')
print('')
print('<!DOCTYPE html>')
print('<html>')
print('<head> <title> Easter Dates </title> ')
print('<meta name ="viewport" content = "width=device-width, initial scale=1"> <link rel="stylesheet" type="text/css" href="../style.css"/>  </head>')
print('<body>')
print('<header><h1>Easter Date Calculator</h1><hr></header>')
print('<p>')
print('The Easter of %s is: <br> <span class="big">%s</span><br><br>' % (year, thedate))
print('<a href="../index.html"> <button type="button">Go Back</button> </a>')
print('</p>')
print('</body>')
print('</html>')
