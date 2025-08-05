import qrcode

link = "megadeth-page.vercel.app" #link de lo que quieras hacer el qr
qr = qrcode.make(link)
qr.save("codigo.png")
