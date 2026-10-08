from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import cm

pdf_path = "/mnt/data/HCI_Chapters_1_2_3_Exam_Notes.pdf"

styles = getSampleStyleSheet()
title = ParagraphStyle("TitleCustom", parent=styles["Title"], alignment=TA_CENTER, fontSize=20, leading=24, spaceAfter=14)
h1 = ParagraphStyle("H1", parent=styles["Heading1"], fontSize=16, leading=20, spaceBefore=12, spaceAfter=8)
h2 = ParagraphStyle("H2", parent=styles["Heading2"], fontSize=13, leading=17, spaceBefore=9, spaceAfter=5)
body = ParagraphStyle("Body", parent=styles["BodyText"], fontSize=9.5, leading=14, spaceAfter=5)
bullet = ParagraphStyle("Bullet", parent=body, leftIndent=14, firstLineIndent=-7, bulletIndent=5)
small = ParagraphStyle("Small", parent=body, fontSize=8.5, leading=12)
important = ParagraphStyle("Important", parent=body, backColor=colors.whitesmoke, borderPadding=6, spaceBefore=5, spaceAfter=7)

doc = SimpleDocTemplate(pdf_path, pagesize=A4, rightMargin=1.5*cm, leftMargin=1.5*cm, topMargin=1.5*cm, bottomMargin=1.5*cm)
story = []

def add_h1(t): story.append(Paragraph(t, h1))
def add_h2(t): story.append(Paragraph(t, h2))
def add_p(t): story.append(Paragraph(t, body))
def add_b(t): story.append(Paragraph("• " + t, bullet))
def add_imp(t): story.append(Paragraph("⭐ " + t, important))

story.append(Paragraph("Human–Computer Interaction (HCI)", title))
story.append(Paragraph("Exam Notes — Chapters 1, 2 & 3", ParagraphStyle("sub", parent=body, alignment=TA_CENTER, fontSize=12, leading=16)))
story.append(Spacer(1, 10))
add_p("Based on the uploaded Alan Dix et al. HCI textbook. These notes are simplified for exam preparation while retaining important terminology and concepts.")
story.append(PageBreak())

# Chapter 1
add_h1("CHAPTER 1 — THE HUMAN")
add_p("Chapter 1 focuses on the human side of HCI: human perception, input/output channels, memory, thinking, problem solving, emotion, individual differences and psychology in interactive-system design.")
add_h2("1.1 Introduction")
add_p("Humans are the most important part of an interactive system. Designers need to understand what users can perceive, remember, think about and physically do.")
add_p("<b>Model Human Processor:</b> a useful model containing three broad systems:")
for x in ["Perceptual system — receives information.", "Cognitive system — processes and interprets information.", "Motor system — controls physical actions."]:
    add_b(x)
add_p("Example: See a button → understand it → move the hand → click.")

add_h2("1.2 Input–Output Channels")
add_p("Important human channels in HCI are vision, hearing and touch, together with physical movement.")
add_h2("Vision")
add_p("Vision involves physical reception by the eye and processing/interpretation by the brain.")
for x in ["Rods — sensitive to light, useful in low light, poor at fine detail and color.", "Cones — provide detailed and color vision and are concentrated around the fovea.", "Visual acuity — ability to see fine detail.", "Visual angle — depends on object size and distance.", "Size constancy — objects are perceived as having relatively constant size despite distance changes.", "Brightness, luminance and contrast affect readability.", "Color can be described using hue, intensity and saturation.", "Do not use color as the only way to communicate important information."]:
    add_b(x)
add_imp("Visual perception is not a perfect copy of the physical world; the brain interprets incomplete and ambiguous information.")
add_h2("Hearing")
for x in ["Pitch — related to frequency.", "Loudness — related to amplitude.", "Timbre — helps distinguish sounds with similar pitch and loudness.", "Cocktail party effect — ability to focus on one conversation/sound among competing sounds.", "Sound can provide attention, status, confirmation and navigation cues."]:
    add_b(x)
add_h2("Touch / Haptic Perception")
for x in ["Thermoreceptors — heat and cold.", "Nociceptors — intense pressure, heat and pain.", "Mechanoreceptors — pressure.", "Kinesthesis — awareness of body position and movement."]:
    add_b(x)
add_h2("Movement")
add_p("Reaction time is the time required to respond to a stimulus. Movement time is the time required to physically move to a target.")
add_imp("Fitts' Law: movement time depends on the distance to a target and the target's size. Large, nearby targets are generally faster/easier to select than small, distant targets.")

add_h2("1.3 Human Memory")
add_p("Three major memory functions are sensory memory, short-term/working memory and long-term memory.")
add_h2("Sensory Memory")
add_p("Temporarily stores information from the senses. Important forms include iconic (visual), echoic (auditory) and haptic (touch) memory. Attention helps information move into short-term memory.")
add_h2("Short-Term / Working Memory")
add_p("A temporary working area with limited duration and capacity.")
add_b("7 ± 2 rule: roughly 5–9 chunks can be held, rather than necessarily 5–9 individual items.")
add_b("Chunking: grouping information into meaningful units.")
add_b("Recognition is generally easier than recall.")
add_h2("Long-Term Memory")
for x in ["Episodic memory — events and personal experiences.", "Semantic memory — facts, concepts and general knowledge.", "Semantic networks — connected representations of knowledge.", "Frames — structured knowledge with slots.", "Scripts — stereotypical sequences of events or actions.", "Production rules — condition–action representations of procedural knowledge."]:
    add_b(x)
add_h2("Forgetting and Retrieval")
for x in ["Storage — information can move into long-term memory through learning/rehearsal.", "Decay — information may weaken over time.", "Interference — other information can make retrieval harder.", "Recall — produce information from memory.", "Recognition — identify information when it is presented."]:
    add_b(x)
add_h2("1.4 Thinking: Reasoning and Problem Solving")
for x in ["Deductive reasoning — general rule → specific conclusion.", "Inductive reasoning — specific observations → general conclusion.", "Problem space — initial state, goal state and operators/actions.", "Analogy — using knowledge from a similar problem to solve a new one.", "Skill acquisition — experience allows users to recognize patterns and perform tasks more efficiently."]:
    add_b(x)
add_h2("Human Error")
add_imp("<b>Slip:</b> correct goal/intention but incorrect execution.")
add_imp("<b>Mistake:</b> incorrect understanding, decision or goal.")
add_h2("1.5 Emotion")
add_p("Emotion affects attention, motivation, performance, decision making and willingness to use a system.")
add_h2("1.6 Individual Differences")
add_p("Users differ in physical and intellectual capabilities and may also differ because of fatigue, stress, illness, distraction or age. Interfaces should not assume all users behave identically.")
add_h2("1.7 Psychology and Design")
add_p("Psychology helps designers understand perception, memory, thinking, learning and error. Principles should be applied with attention to context and evidence.")
story.append(PageBreak())

# Chapter 2
add_h1("CHAPTER 2 — THE COMPUTER")
add_p("Chapter 2 examines the computer side of HCI: input devices, pointing devices, displays, VR/3D devices, physical controls and sensors, paper, memory, processing and networks.")
add_h2("2.1 Introduction")
add_p("Computer interaction involves input, output and internal processing. Input includes keyboards, mice, touch and speech; output includes displays, sound and paper.")
add_h2("Batch Processing")
add_p("In batch processing, a collection of information is submitted for processing and the user may wait for the result. Modern interactive systems aim for much more immediate feedback.")
add_h2("2.2 Text Entry Devices")
for x in ["QWERTY keyboard — dominant traditional keyboard layout.", "DVORAK — alternative layout designed to improve typing efficiency.", "Chord keyboard — combinations of keys produce characters; compact but difficult to learn.", "Numeric keypads — calculator and telephone layouts are common.", "T9 — predictive phone text entry.", "Handwriting recognition — converts pen/stylus writing to text; accuracy varies with handwriting.", "Speech recognition — useful for hands-free or accessibility scenarios but affected by noise, accents and ambiguity."]:
    add_b(x)
add_h2("2.3 Positioning, Pointing and Drawing")
for x in ["Mouse — indirect pointing device; accurate and common.", "Touchpad — touch-sensitive surface controlling a pointer.", "Trackball — ball remains in its housing; compact.", "Joystick — useful especially for games; may control position or velocity.", "Touchscreen — direct input; easy to learn but finger can obscure the display and may be inaccurate for small targets.", "Stylus/light pen — useful for accurate pointing and drawing.", "Digitizing tablet — useful for freehand drawing and CAD.", "Eyegaze — tracks where the user is looking; useful in some accessibility scenarios but requires calibration."]:
    add_b(x)
add_h2("2.4 Display Devices")
for x in ["CRT — electron beam and phosphor-based display; historically bulky and heavy.", "LCD — flat-panel, thin and light.", "Resolution — number of available pixels.", "Pixel — smallest addressable element of a bitmap display.", "Refresh rate — frequency at which the display is updated.", "Flicker — visible variation associated with refreshing.", "Contrast — difference between foreground and background brightness.", "Anti-aliasing — smooths jagged diagonal/curved lines."]:
    add_b(x)
add_h2("2.5 Virtual Reality and 3D Interaction")
add_p("3D interaction can involve a 3D mouse, dataglove, head-mounted display and body tracking.")
add_imp("Six degrees of freedom = 3 positional dimensions (X, Y, Z) + 3 rotational dimensions (pitch, yaw, roll).")
add_h2("2.6 Physical Controls, Sensors and Special Devices")
add_p("Computers can interact with the physical world through buttons, switches, knobs, sensors and haptic devices.")
add_p("Sensors may detect temperature, movement, location, weight, light, sound, video and other environmental or physiological information.")
add_p("Haptic feedback provides physical/tactile feedback to the user.")
add_h2("2.7 Paper: Printing and Scanning")
add_p("Printers include dot matrix, inkjet and laser technologies. Scanners convert physical documents/images into digital information. Readability depends on font, size, spacing, contrast and layout.")
add_h2("2.8 Computer Memory")
add_p("Memory capacity and access speed affect the size and responsiveness of applications. RAM provides fast working memory; long-term storage includes devices such as hard disks and optical storage.")
add_h2("2.9 Processing and Networks")
add_p("Processor speed affects response time, but memory, graphics, storage and networks can also become bottlenecks.")
add_imp("Myth of the infinitely fast machine: designers should not assume every operation will be instantaneous. Slow operations should provide feedback such as progress indicators or status messages.")
add_p("Networks allow computers to communicate and share resources. TCP/IP is the main protocol suite discussed for Internet communication.")
story.append(PageBreak())

# Chapter 3
add_h1("CHAPTER 3 — THE INTERACTION")
add_p("Chapter 3 studies communication between the human and the computer through interaction models, HCI frameworks, ergonomics, interaction styles, WIMP, interactivity, context and user experience.")
add_h2("3.1 Introduction")
add_p("Interaction ranges from low-interaction batch processing to highly interactive systems with continuous input and feedback.")
add_h2("3.2 Models of Interaction")
add_imp("Norman's Execution–Evaluation Cycle: Goal → form intention → specify action → execute action → system changes → observe output → interpret output → evaluate result.")
add_h2("Gulf of Execution")
add_p("The gulf of execution is the difficulty of translating the user's goal into actions supported or communicated by the interface.")
add_h2("Gulf of Evaluation")
add_p("The gulf of evaluation is the difficulty of understanding the system's resulting state from its output.")
add_h2("Four Important Translations")
for x in ["Articulation — user expresses the intended input.", "Performance — system carries out the input.", "Presentation — system presents its result.", "Observation — user perceives/interprets the result."]:
    add_b(x)
add_h2("3.3 Frameworks and HCI")
add_p("The interaction framework considers the user, input, system and output and the translations between them. It also recognizes wider social and organizational context.")
add_h2("3.4 Ergonomics")
add_p("Ergonomics concerns the physical characteristics of interaction and their effects on performance.")
for x in ["Arrangement of controls and displays.", "Physical environment such as lighting, noise, temperature and workspace.", "Health issues such as fatigue and repetitive strain.", "Careful use of color and consideration of different visual capabilities."]:
    add_b(x)
add_h2("3.5 Interaction Styles")
for x in ["Command line — powerful and efficient for experts but requires command knowledge.", "Menus — visible choices, easier for beginners, but large/hierarchical menus can become difficult.", "Natural language — familiar but can be ambiguous.", "Question/answer — simple for restricted tasks.", "Query language — powerful information retrieval but requires syntax knowledge.", "Form filling — familiar and effective for structured data entry.", "Spreadsheets — grid-based interaction with formulas and immediate feedback.", "WIMP — Windows, Icons, Menus and Pointers.", "Point-and-click — direct selection of objects/links.", "3D interfaces — interaction with three-dimensional environments."]:
    add_b(x)
add_h2("WIMP")
add_imp("WIMP = Windows + Icons + Menus + Pointers.")
for x in ["Windows — separate areas for applications/information.", "Icons — graphical representations of objects or actions.", "Menus — lists of available options/commands.", "Pointers — indicate the location of interaction.", "Buttons, toolbars, dialog boxes and palettes are additional common graphical elements."]:
    add_b(x)
add_h2("3.6 WIMP Elements")
add_p("Remember: Windows, Icons, Menus, Pointers. Also know buttons, toolbars, dialog boxes and palettes.")
add_h2("3.7 Interactivity")
add_p("Interactivity concerns how the system responds to user actions and how the user and system influence each other over time. Two interfaces can have the same visible elements but feel different because their behavior differs.")
add_p("User initiative is important: users normally initiate actions in modern WIMP environments, although modal dialogs can temporarily restrict interaction.")
add_h2("3.8 Context of Interaction")
for x in ["Physical context — lighting, noise, location, available space and mobility.", "Social context — other people can affect interaction.", "Organizational context — roles, rules and workplace practices affect use."]:
    add_b(x)
add_h2("3.9 Experience, Engagement and Fun")
add_p("Modern HCI considers not only task completion but also enjoyment, engagement, motivation, experience, emotional response and value.")
story.append(PageBreak())

# Comparisons
add_h1("IMPORTANT EXAM COMPARISONS")
def comparison(title_text, rows):
    add_h2(title_text)
    data = [[Paragraph("<b>Concept A</b>", small), Paragraph("<b>Concept B</b>", small)]]
    for a,b in rows:
        data.append([Paragraph(a, small), Paragraph(b, small)])
    t = Table(data, colWidths=[8.5*cm,8.5*cm])
    t.setStyle(TableStyle([
        ("GRID",(0,0),(-1,-1),0.5,colors.grey),
        ("BACKGROUND",(0,0),(-1,0),colors.lightgrey),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("LEFTPADDING",(0,0),(-1,-1),5),
        ("RIGHTPADDING",(0,0),(-1,-1),5),
    ]))
    story.append(t)
    story.append(Spacer(1,8))

comparison("Recall vs Recognition", [
    ("Produce information from memory.", "Identify information when it is presented."),
    ("Generally harder.", "Generally easier."),
    ("Example: remember a command.", "Example: select a command from a menu.")
])
comparison("Slip vs Mistake", [
    ("Correct intention, wrong execution.", "Incorrect understanding/decision/goal."),
    ("Example: click the wrong button.", "Example: misunderstand an icon.")
])
comparison("Mouse vs Touchscreen", [
    ("Indirect input.", "Direct input."),
    ("Separate pointing device.", "Finger/stylus points directly."),
    ("Generally accurate for small targets.", "Finger may be inaccurate and obscure screen.")
])
comparison("Command Line vs Menu", [
    ("User types commands.", "User selects visible options."),
    ("Requires more recall.", "Supports recognition."),
    ("Powerful for experts.", "Generally easier for beginners.")
])

add_h1("TOP EXAM QUESTIONS")
questions = [
"Explain the Model Human Processor.","Explain human input/output channels.","Differentiate rods and cones.",
"Explain Fitts' Law and its importance in HCI.","Explain sensory, short-term and long-term memory.",
"Explain the 7 ± 2 rule and chunking.","Differentiate recall and recognition.",
"Explain semantic networks, frames and scripts.","Explain problem space and problem solving.",
"Differentiate slips and mistakes.","Explain QWERTY and DVORAK keyboards.",
"Explain T9, handwriting recognition and speech recognition.","Compare mouse, touchscreen, touchpad and trackball.",
"Explain display characteristics.","Explain six degrees of freedom.","Explain sensors and haptic feedback.",
"Explain the myth of the infinitely fast machine.","Explain Norman's execution-evaluation cycle.",
"Explain the gulf of execution and gulf of evaluation.","Explain the interaction framework.",
"What is ergonomics?","Explain different interaction styles.","What is WIMP? Explain its elements.",
"Explain interactivity and user initiative.","Explain the physical, social and organizational context of interaction."
]
for i,q in enumerate(questions,1):
    add_p(f"<b>{i}. {q}</b>")

add_h1("LAST-DAY REVISION")
for x in [
"Chapter 1: Human → Perception → Memory → Thinking → Emotion → Individual differences.",
"Memory: Sensory → Short-term/Working → Long-term.",
"Fitts' Law: bigger and closer targets are generally faster to select.",
"Slip = correct goal, wrong execution. Mistake = wrong understanding/decision.",
"Chapter 2: Input devices + output devices + displays + 3D/VR + sensors + memory + processing + networks.",
"3D interaction: 6 degrees of freedom = 3 translation + 3 rotation.",
"Never assume an infinitely fast computer; account for delays and provide feedback.",
"Chapter 3: Human + Computer = Interaction.",
"Norman: Goal → Action → System → Output → Evaluation.",
"Gulf of Execution = difficulty doing what you want. Gulf of Evaluation = difficulty understanding what happened.",
"WIMP = Windows + Icons + Menus + Pointers.",
"Ergonomics = physical aspects of interaction.",
"Context = physical + social + organizational environment."
]:
    add_imp(x)

doc.build(story)
print(pdf_path)
