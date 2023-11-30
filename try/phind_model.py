import re

text = """
Abandonado, s. adj. El que no tiene favores que otorgar. Des-
provisto de fortuna. Amigo de la verdad y el sentido común.
Abdicación, s. Acto mediante el cual un soberano demuestra per-
cibir la alta temperatura del trono.
Abdomen, s. Templo del dios Estomago, al que rinden culto y
sacrificio todos los hombres auténticos. Las mujeres sólo prestan a esta
antigua fe un sentimiento vacilante. A veces ofician en su altar, de
modo tibio e ineficaz, pero sin veneración real por la única deidad que
los hombres verdaderamente adoran. Si la mujer manejara a su gusto el
mercado mundial, nuestra especie se volvería graminívora.
Aborígenes, s. Seres de escaso mérito que entorpecen el suelo de
un país recién descubierto. Pronto dejan de entorpecer; entonces, ferti-
lizan.
Abrupto, adj. Repentino, sin ceremonia, como la llegada de un
cañonazo y la partida del soldado a quien está dirigido. El doctor Sa-
muel Johnson, refiriéndose a las ideas de otro autor, dijo hermosa-
mente que estaban “concatenadas sin abrupción”.
Absoluto, adj. Independiente, irresponsable. Una monarquía ab-
soluta es aquella en que el soberano hace lo que le place, siempre que
él plazca a los asesinos. No quedan muchas: la mayoría han sido reem-
plazadas por monarquías limitadas, donde el poder del soberano para
hacer el mal (y el bien) está muy restringido; o por repúblicas, donde
gobierna el azar.
"""

matches = re.findall(r"^[A-Za-z]+\,\s[a-z\s[.]]*", text, re.MULTILINE)

for match in matches:
    print(
        match
    )  # prints: ['Abandonado, s. adj. El que no tiene favores que otorgar. Des-', 'Abdicación, s. Acto mediante el cual un soberano demuestra per-', 'Abdomen, s. Templo del dios Estomago, al que rinden culto y', 'Aborígenes, s. Seres de escaso mérito que entorpecen el suelo de', 'Abrupto, adj. Repentino, sin ceremonia, como la llegada de un', 'Absoluto, adj. Independiente, irresponsable. Una monarquía ab-']
