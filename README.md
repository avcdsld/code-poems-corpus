# code-poems-corpus

A multi-language collection of 55 *code poems* originally published in  
**_code (poems}_** (Ishac Bertran, 2012), plus a machine-readable TEI edition
with stand-off syntax annotations generated via Tree-sitter.

> **Terminology**  
> *Raw corpus* = verbatim source files in `/corpus_raw`  
> *Annotated corpus* = TEI-XML version in `/corpus_tei` (this is “the corpus” unless stated otherwise)

---

## Directory layout

```
code-poems-corpus/
├── LICENSE # CC BY-NC-ND 3.0 – original poems
├── README.md # ← you are here
├── corpus_raw/ # ① raw corpus
└── corpus_tei/ # ② annotated corpus (TEI + standOff)
```

---

## Licensing

| Path | Contents | License |
|------|----------|---------|
| `/corpus_raw` | Raw corpus – original poems (verbatim) | **CC BY-NC-ND 3.0** |
| `/corpus_tei` | Annotated corpus – TEI markup & metadata* | **CC BY 4.0** |

\* Each TEI file embeds or references the original poem text, which remains under  
CC BY-NC-ND 3.0. Distributing a TEI file together with **modified** poem text requires
permission from the original authors.

---

## Corpus Index (55 items)

| # | Title | Author(s) | Language | File |
|---|---|---|---|---|
| 1 | ARS POETICA | Alejandro Corredor | Processing | `corpus_raw/processing/1_ars_poetica.pde` |
| 2 | UNHANDLED LOVE | Daniel Bezerra | C++ | `corpus_raw/cpp/2_unhandled_love.cpp` |
| 3 | BODY | Carrie Padian | HTML | `corpus_raw/html/3_body.html` |
| 4 | RACING NUMBERS | Gerrit Riessen | Shell | `corpus_raw/sh/4_racing_numbers.sh` |
| 5 | DISFUNCTION() | Brad Sorensen | JavaScript | `corpus_raw/js/5_disfunction.js` |
| 6 | IMPORT SOUL | Richard Littauer | Python | `corpus_raw/python/6_import_soul.py` |
| 7 | MARY.LAMB | James Grant | C++ | `corpus_raw/cpp/7_mary.lamb.cpp` |
| 8 | FLUENT.SHE.SHARPLY | Matthew Perkins | C# | `corpus_raw/csharp/8_fluent.she.sharply.cs` |
| 9 | UNTITLED (LOVE) | Nataliya Petkova | Processing | `corpus_raw/processing/9_untitled_love.pde` |
| 10 | 1701998444 | Marco Triverio | C | `corpus_raw/c/10_1701998444.c` |
| 11 | EUCLID IN DISGUISE | Yves Daoust | C | `corpus_raw/c/11_euclid_in_disguise.c` |
| 12 | FOLLOW ME TO THE DEN OF ZEN… | Nemesis Fixx | Ruby | `corpus_raw/ruby/12_follow_me_to_the_den_of_zen.rb` |
| 13 | ISM &#124; BREATH &#124; WHO &#124; SHE &#124; WITH &#124; I | Nancy Mauro-Flude | *nix | `corpus_raw/nix/13_ism_breath_who_she_with_i.nix` |
| 14 | TWOFACED | Jason Kopylec | Java | `corpus_raw/java/14_twofaced.java` |
| 15 | BITS OF THE UNIVERSE | Elena Machkasova | Clojure | `corpus_raw/clojure/15_bits_of_the_universe.clj` |
| 16 | LIFE IS RANDOM | Ubaldo Pescatore | Java | `corpus_raw/java/16_life_is_random.java` |
| 17 | FOR AGNES | Jeffrey Knight | Shell (macOS) | `corpus_raw/sh_mac/17_for_agnes.sh` |
| 18 | SIMPLIFY | Josh Fongheiser | Visual Basic | `corpus_raw/vb/18_simplify.vb` |
| 19 | TWO STEPS FORWARD | Aaron Broder | C | `corpus_raw/c/19_two_steps_forward.c` |
| 20 | RISING | Vilson Vieira, Renato Fabbri | Python | `corpus_raw/python/20_rising.py` |
| 21 | OSLO | David Berry | Ruby | `corpus_raw/ruby/21_oslo.rb` |
| 22 | THE RUMOR | Pall Thayer | Perl | `corpus_raw/perl/22_the_rumor.pl` |
| 23 | JUDGMENT | Guilherme Kerr | JavaScript | `corpus_raw/js/23_judgment.js` |
| 24 | NESTING | Dan Brown | HTML | `corpus_raw/html/24_nesting.html` |
| 25 | THE GAME | Ryan Christiansen | Rebol | `corpus_raw/rebol/25_the_game.reb` |
| 26 | A VOLATILE SKETCHBOOK | Aymeric Mansoux | Forth | `corpus_raw/forth/26_a_volatile_sketchbook.fs` |
| 27 | N/A | Joaquim d'Souza | Java | `corpus_raw/java/27_na.java` |
| 28 | AS3, STILL ALIVE | Jonny Plackett | ActionScript 3 | `corpus_raw/as/28_as3_still_alive.as` |
| 29 | RULE 30 | Shawn Lawson | C++ | `corpus_raw/cpp/29_rule_30.cpp` |
| 30 | VARIATIONS ON A QUINE, IN PY MINOR | Rafael Romero | Python | `corpus_raw/python/30_variations_on_a_quine,_in_py_minor.py` |
| 31 | TIME GOES BY SLOWLY | Chris Boucher | Visual Basic | `corpus_raw/vb/31_time_goes_by_slowly.vb` |
| 32 | VAN[ ]SH | Thibault Autheman | Processing | `corpus_raw/processing/32_van_sh.pde` |
| 33 | CESARE PAVESE'S STUBBORNNESS | Ruggero Castagnola | Processing | `corpus_raw/processing/33_cesare_paveses_stubborness.pde` |
| 34 | AN OCEAN OF INTEGER WAVES | Matthew Ward | Java | `corpus_raw/java/34_an_ocean_of_integer_waves.java` |
| 35 | IMMEDIATE FUNCTION | Marcus Ross | JavaScript | `corpus_raw/js/35_immediate_function.js` |
| 36 | HTML = HELLO TODAY MEANS LATER | Viviana Alvarez | HTML | `corpus_raw/html/36_html_hello_today_means_later.html` |
| 37 | BASICHELL | Wolf Herrera | DOS Batch | `corpus_raw/dos/37_basichell.bat` |
| 38 | OH MINI 8-BALL | Michael Fall | Pascal | `corpus_raw/pascal/38_oh_mini_8-ball.pas` |
| 39 | SATURDAY, FIRST LIGHT | Jennifer Mace | C | `corpus_raw/c/39_saturday_first_light.c` |
| 40 | BUDDHISTLIFE | Thomas Braun | Java | `corpus_raw/java/40_buddhistlife.java` |
| 41 | BODYCLOCK | Dom Slatford | C# | `corpus_raw/csharp/41_bodyclock.cs` |
| 42 | REALITY | David Sjunnesson | Processing | `corpus_raw/processing/42_reality.pde` |
| 43 | HOW TO CHOOSE A LOVER WITH SQL | David Devanny | SQL | `corpus_raw/sql/43_how_to_choose_a_lover_with_sql.sql` |
| 44 | SLEEPINGTHROUGHLIFE | Jot Kali | C | `corpus_raw/c/44_sleepingthroughlife.c` |
| 45 | DAILYGRIND | Paul Illingworth | Java | `corpus_raw/java/45_dailygrind.java` |
| 46 | FOREVER | Mario Sangiorgio | C | `corpus_raw/c/46_forever.c` |
| 47 | SHORT TRIPS | the55 | JavaScript | `corpus_raw/js/47_short_trips.js` |
| 48 | ENDET | Sylke Boyd | Fortran 90 | `corpus_raw/fortran90/48_endet.f90` |
| 49 | OPTIMIZE ME | Daniel Bezerra | C++ | `corpus_raw/cpp/49_optimize_me.cpp` |
| 50 | INSERT IGNORANCE INTO IGNORANCE | Ed Schenk | Processing | `corpus_raw/processing/50_insert_ignorance_into_ignorance.pde` |
| 51 | LOVE WILL TEAR US APART | Jerome Saint-Clair | Java | `corpus_raw/java/51_love_will_tear_us_apart.java` |
| 52 | DESPERATE PROGRAM | John Saylor | JavaScript | `corpus_raw/js/52_desperate_program.js` |
| 53 | EPISTLE | Yann van der Cruyssen | C++ | `corpus_raw/cpp/53_epistle.cpp` |
| 54 | DANCING WITHIN | Álvaro Matías Wong Díaz | C# | `corpus_raw/csharp/54_dancing_within.cs` |
| 55 | CREATION? | Kenny Brown | Python | `corpus_raw/python/55_creation.py` |

---

### How to regenerate the annotated corpus (quick start)

```bash
pyenv install 3.11
python3.11 -m venv venv && source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python tools/parser/parse_corpus.py

deactivate
```
