def main():
    english_matt_6_14 = "For if ye forgive men their trespasses, your heavenly Father will also forgive you\n"
    greek_matt_6_14 = "ἐὰν γὰρ ἀφῆτε τοῖς ἀνθρώποις τὰ παραπτώματα αὐτῶν, ἀφήσει καὶ ὑμῖν ὁ πατὴρ ὑμῶν ὁ οὐράνιος\n"
    deseret_3_nephi_13_14 = "𐐙𐐫𐑉, 𐐮𐑁 𐐷 𐑁𐐲𐑉𐑀𐐮𐑂 𐑋𐐯𐑌 𐑄𐐯𐑉 𐐻𐑉𐐯𐑅𐐹𐐰𐑅𐐮𐑆, 𐐷𐐫𐑉 𐐸𐐯𐑂𐐲𐑌𐑊𐐨 𐐙𐐱𐑄𐐲𐑉 𐐶𐐮𐑊 𐐫𐑊𐑅𐐬 𐑁𐐲𐑉𐑀𐐮𐑂 𐐷𐐭\n"

    with open("forgive.txt", mode="wt", encoding="utf_8", newline="\n") as outf:
        outf.write(english_matt_6_14)
        outf.write(greek_matt_6_14)
        outf.write(deseret_3_nephi_13_14)

main()
