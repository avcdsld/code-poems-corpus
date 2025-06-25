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
├── LICENSE                     # CC BY-NC-ND 3.0 – original poems
├── README.md                   # ← you are here
├── requirements.txt            # Python dependencies
├── analyze_displacement.py     # Main analysis script
├── config.yml                  # Configuration file
├── corpus_raw/                 # ① raw corpus (original poems)
├── corpus_processed/           # ② tree-sitter parsed data (AST/tokens)
├── corpus_tei/                 # ③ annotated corpus (TEI + standOff)
├── tools/                      # analysis and processing pipeline
│   ├── displacement_analysis.py   # core displacement detection
│   ├── displacement_patterns.py   # pattern definitions
│   ├── visualization.py           # HTML visualization
│   └── parser/                     # corpus processing tools
├── docs/                       # theoretical documentation
└── output/                     # generated analysis results
    ├── analysis/               # JSON analysis data
    ├── ast/                    # syntax tree outputs
    ├── visualization/          # HTML visualizations
    └── comparison/             # comparative analysis
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
| 23 | JUDGMENT | Guilherme Kerr | HTML | `corpus_raw/html/23_judgment.html` |
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

```bash
python -m tools.parser.parse_corpus --lang js
python tools/parser/list_node_types.py
python tools/parser/annotate_ast.py
```

---

## Semiotic Displacement Analysis

This repository includes a **semiotic displacement analysis system** based on Charles Sanders Peirce's sign classification theory, designed to study the poetic effects in code poetry through quantitative analysis of sign transformations.

### Theoretical Framework

The system applies Peirce's triadic sign classification to programming code:

- **Icon** (類像): Literal values, comments → direct resemblance to objects
- **Index** (指標): Variable names, function names → causal relationship to objects  
- **Symbol** (象徴): Keywords, operators → conventional meaning relationship

**Semiotic Displacement** is defined as the deviation from expected sign classification during code execution, which creates poetic effects in code poetry.

### Quick Analysis

#### 1. AST Output (Syntax Analysis)
```bash
# List available poems
python analyze_displacement.py list

# View syntax analysis results only
python analyze_displacement.py ast 5_disfunction
python analyze_displacement.py ast 5_disfunction --lang js

# Save AST to file
python analyze_displacement.py ast 5_disfunction --output file
```

#### 2. Displacement Analysis
```bash
# Analyze semiotic displacements
python analyze_displacement.py analyze 5_disfunction
python analyze_displacement.py analyze 52_desperate_program

# Analyze with automatic visualization
python analyze_displacement.py analyze 5_disfunction --viz
```

#### 3. Interactive Visualization
```bash
# Generate HTML visualization
python analyze_displacement.py visualize 5_disfunction
python analyze_displacement.py visualize 52_desperate_program

# Open generated HTML files in browser
open 5_disfunction_displacement_visualization.html
open 52_desperate_program_displacement_visualization.html
```

#### 4. Comparative Analysis
```bash
# Compare multiple poems
python analyze_displacement.py compare 5_disfunction 52_desperate_program 35_immediate_function

# Results saved to poem_comparison_N_works.json
```

### Analysis Results

The system detects various displacement patterns:

| Pattern | Description | Example |
|---------|-------------|---------|
| **Emotional Expression** | Variables expressing emotional states | `weCannotStart`, `iCannotRun` |
| **Visual Poetry** | Syntactic structures creating visual effects | Nested if/while statements |
| **Metaphorical Syntax** | Program constructs used metaphorically | `catch(me)` - personification |
| **Semantic Inversion** | Abstract concepts as concrete variables | `[anything, something, whatever]` |
| **Temporal Expression** | Code structures expressing time/duration | Repetitive loops, sequential actions |

### Currently Analyzed Works

| Work | Displacements | Max Intensity | Dominant Patterns |
|------|---------------|---------------|-------------------|
| `5_disfunction` | 26 | 0.95 | Visual poetry, metaphorical syntax |
| `52_desperate_program` | 13 | 0.85 | Semantic inversion, emotional expression |
| `35_immediate_function` | 0 | - | Technical code (no poetic displacement) |

### Output Files

- **`output/ast/{poem_id}_ast_{lang}.txt`**: Syntax analysis (AST) output files
- **`output/analysis/{poem_id}_displacement_analysis.json`**: Detailed displacement analysis data
- **`output/visualization/{poem_id}_displacement_visualization.html`**: Interactive visualization with statistics
- **`output/comparison/poem_comparison_N_works.json`**: Comparative analysis results
- **Console output**: Summary statistics and top displacement events

> **Note**: Output files are organized in the `output/` directory and can be safely deleted after use. They are automatically recreated when running analysis commands.

### Research Applications

This system enables quantitative analysis for:

- **Literary criticism**: Measuring poetic effects in code poetry
- **Computational aesthetics**: Understanding human-computer interaction through poetry
- **Semiotic theory**: Validating Peirce's sign theory in digital contexts
- **Reader studies**: Correlating displacement patterns with reader attention

### Advanced Usage

#### Custom Displacement Detection
```bash
# Modify detection patterns in:
tools/displacement_patterns.py

# Add new poetry patterns to:
self.patterns = {
    'your_pattern': [...],
}
```

#### Extending to Other Languages
```bash
# Add language support in:
tools/parser/plugins/your_language.py

# Update configuration:
config.yml
```

### Installation

```bash
# Clone repository
git clone https://github.com/username/code-poems-corpus.git
cd code-poems-corpus

# Set up Python environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

### Dependencies

The core dependencies are listed in `requirements.txt`:

```bash
tree-sitter>=0.20.0
tree-sitter-languages>=1.5.0
PyYAML>=6.0
```

Optional dependencies for advanced analysis:
```bash
pip install numpy pandas matplotlib
```

### Research Citation

If you use this displacement analysis system in your research, please cite:

```
[Your research paper on semiotic displacement in code poetry]
"Semiotic Displacement and Peirce's Sign Classification in Code Poetry"
```