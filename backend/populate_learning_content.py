import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from learning.models import Lesson, Quiz

def populate_learning():
    # Clear existing data
    Lesson.objects.all().delete()
    Quiz.objects.all().delete()

    print("Populating Professional EDC Curriculum...")

    # Phase 1
    l1 = Lesson.objects.create(
        title="Atomic Physics & Energy Bands",
        content="""
        <div class='space-y-4'>
            <p>Every atom defines its behavior through its electron configuration. In solids, individual energy levels blur into <strong>Energy Bands</strong>.</p>
            <h3>Bands and Gaps</h3>
            <p>The <strong>Valence Band</strong> is the highest range of electron energies where electrons are normally present. The <strong>Conduction Band</strong> is the range where electrons can move freely. The distance between them is the <strong>Band Gap (Eg)</strong>.</p>
            <ul class='list-disc pl-5'>
                <li><strong>Conductors:</strong> Bands overlap (Eg = 0).</li>
                <li><strong>Insulators:</strong> Large gap (Eg > 5 eV).</li>
                <li><strong>Semiconductors:</strong> Small gap (Eg ≈ 1.1 eV for Silicon).</li>
            </ul>
        </div>
        """,
        order=1
    )
    Quiz.objects.create(lesson=l1, question="In which region must an electron be to contribute to electrical conduction?", options=["Valence Band", "Depletion Region", "Conduction Band", "Atomic Nucleus"], correct_option_index=2, xp_reward=50)

    # Phase 2
    l2 = Lesson.objects.create(
        title="Semiconductor Physics: Doping",
        content="""
        <div class='space-y-4'>
            <p>Pure semiconductors (Intrinsic) have limited use. We improve them through <strong>Doping</strong>.</p>
            <h3>Extrinsic Semiconductors</h3>
            <p>By adding Group V elements (Phosphorus), we create <strong>N-type</strong> material (extra electrons). Adding Group III elements (Boron) creates <strong>P-type</strong> material (holes).</p>
            <p>The <strong>Fermi Level (Ef)</strong> represents the probability of finding an electron. In N-type, Ef moves toward the Conduction Band; in P-type, it moves toward the Valence Band.</p>
        </div>
        """,
        order=2
    )
    Quiz.objects.create(lesson=l2, question="What is the majority carrier in a P-type semiconductor?", options=["Electrons", "Holes", "Protons", "Neutrons"], correct_option_index=1, xp_reward=75)

    # Phase 3
    l3 = Lesson.objects.create(
        title="Carrier Transport: Drift & Diffusion",
        content="""
        <div class='space-y-4'>
            <p>How do carriers move? There are two primary mechanisms: <strong>Drift</strong> and <strong>Diffusion</strong>.</p>
            <h3>1. Drift Current</h3>
            <p>Motion caused by an external <strong>Electric Field</strong>. carriers move with a 'drift velocity' determined by their mobility (μ).</p>
            <h3>2. Diffusion Current</h3>
            <p>Motion caused by a <strong>Concentration Gradient</strong>. Carriers move from regions of high density to low density.</p>
            <div class='p-4 bg-secondary/10 border border-secondary/20 rounded-xl font-mono text-xs'>
                J_total = J_drift + J_diffusion
            </div>
        </div>
        """,
        order=3
    )

    # Phase 4
    l4 = Lesson.objects.create(
        title="The PN Junction Physics",
        content="""
        <div class='space-y-4'>
            <p>When P and N materials meet, a <strong>Depletion Region</strong> forms at the interface as electrons and holes recombine.</p>
            <h3>Barrier Potential</h3>
            <p>This creates an internal electric field that prevents further carrier flow. For Silicon, this barrier is typically <strong>0.7V</strong>.</p>
            <ul class='list-disc pl-5'>
                <li><strong>Forward Bias:</strong> Reduces the barrier, allowing current flow.</li>
                <li><strong>Reverse Bias:</strong> Increases the barrier, blocking current.</li>
            </ul>
        </div>
        """,
        order=4
    )
    Quiz.objects.create(lesson=l4, question="What is the typical barrier potential for a Silicon PN junction at room temperature?", options=["0.3V", "0.7V", "1.1V", "5.0V"], correct_option_index=1, xp_reward=100)

    # Phase 5
    l5 = Lesson.objects.create(
        title="Transistors & Modern Circuits",
        content="""
        <div class='space-y-4'>
            <p>The <strong>Transistor</strong> is the most important invention of the 20th century. It acts as a controlled switch or amplifier.</p>
            <h3>BJT and MOSFET</h3>
            <p><strong>BJT (Bipolar Junction Transistor)</strong> uses both electrons and holes. <strong>MOSFET (Metal-Oxide-Semiconductor FET)</strong> is the standard for modern ICs, controlled by a voltage at the Gate.</p>
             <div class='mt-6 rounded-xl overflow-hidden'>
                <a href='/learning/game/conductivity/' class='block p-4 bg-amber-500 text-dark-950 font-black text-center'>Launch Transistor Challenge Game</a>
            </div>
        </div>
        """,
        order=5
    )

    # Phase 6
    l6 = Lesson.objects.create(
        title="Nano-Electronics & Quantum Effects",
        content="""
        <div class='space-y-4'>
            <p>As we shrink transistors below 5nm, classical physics breaks down. Enter <strong>Quantum Tunneling</strong>.</p>
            <h3>Future Horizons</h3>
            <p>We are now moving toward <strong>Quantum Dots</strong> and <strong>Nanowire FETs</strong>, where atomic structure isn't just a property—it's the entire device.</p>
        </div>
        """,
        order=6
    )

    print("Success: Advanced EDC curriculum populated!")

if __name__ == "__main__":
    populate_learning()
