# import module
import streamlit as st

# Title
st.title(":orange[just-web]")

# Header
st.header("Haloo..!! Selamat Datang Di :violet[just-web]", divider="violet")

# Sub-header
st.subheader("Disini web ini akan mengedukasi seputar pemrograman web ataupun pemrograman bahasa lainnya")

# Disclamer about wesite
st.write("""Ini adalah pembukaan sekaligus juga untuk pembelajaran pertama yang dilakukan dalam pembuatan web ini,
         Saya mebuat website ini untuk membagikan ilmu saya untuk lebih mengenalkan kepada GENERASI sekarang apa itu bahasa pemrograman.
         sebenarnya bahasa pemrograman itu sangat seru jika kita ingin tahu dan mendalami karena melatih kognitif kita dalam problem solve.
         Dalam dunia coding memang dibutuhkan problem solving("pemecahan masalah") namun itu tidak menjadi penghambat
         untuk kita mempelajari sebuah bahasa pemrograman, karena saya sendiri pun juga sama tapi saya belajar dari bahasa pemrograman
         "tidak selamanya kita mempelajarinya bisa jadi kita belajar dari-nya" """)

st.write("""Untuk penggunaan web lebih lanjut kalian bisa Explore website ini, ataupun 
         kalian bisa klik link ini untuk memulai pembelajaran kalian  """)

# Caption
st.caption("ini komentar :orange[yaa guysss..!!!] :moyai:")

# Pembahasan tentang website ini
st.markdown("## 1. Bagaimana website ini dibuat")
st.write("""WEBSITE ini dibuat dengan bahasa pemrograman python menggunkan streamlit. **python**
         adalah bahasa yang powerfull bahasa inilah yang pertama kali saya pelajari dan menjadi favorit saya,
         walaupun di dunia industri kita tidak kebanykan menggunakan python """)

st.image(image='py.jpg', caption='just ilustration, the picture get from pinterest', width=750)

st.markdown("## 2. mengapa website ini dubuat untuk pembelajaran")
st.write("""Kami akan menyajikan edukasi penting tentang teknologi di era sekarang atau yang akan mendatang,
         web ini dibuat ketika sang develop belajar maka web ini juga akan digunakan untuk belajar""")

st.code(""" import streamlit as st
         st.write("Hello World")""", language='python')

st.write(""" di atas adalah sedikit replika bagaimana awal web ini dibuat.""")

# Page
