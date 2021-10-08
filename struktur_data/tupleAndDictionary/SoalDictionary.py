paragraf = "Barcelona berhasil merebut posisi puncak klasemen La Liga Spanyol seusai menang 4-2 atas Sevilla pada pertandingan pekan kesembilan di Stadion Camp Nou , Sabtu (20/10/2018) atau Minggu dini hari WIB . Barcelona membuka keunggulan pada menit ke-2 melalui gol yang dicetak oleh Philippe Coutinho . Lionel Messi menggandakan keunggulan Barcelona , 10 menit berselang .  Namun , nahas bagi Barcelona , karena Messi harus ditarik keluar pada menit ke-26 setelah mengalami cedera . Tanpa Messi , skor 2-0 bertahan hingga babak pertama berakhir ."

paragraf = paragraf.lower()

lisParagraf = paragraf.split()

dictionary = {}
for i in lisParagraf:
    dictionary[i] = lisParagraf.count(i)

print(dictionary)






