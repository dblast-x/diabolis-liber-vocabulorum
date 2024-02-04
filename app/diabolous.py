"""
Notes:
----------------------------
+++ Diccionario del Diablo || Diablis Liber Vocabulorum +++
 Cli application that acts as a dict
 but instead of the usual definitions
 it maps to Ambrose Bierce's dictionary.
----------------------------
Plan:
    Elements:
    . Diabolous
      . Promt(intro)(question)(exit)
      . Input
      . Search Engine as SE
      . Output(definition)(error as typo)
    .

    Steps:
     loop >>

      when Diabolous.start! =>> Promt.intro!
      .then =>> Promt.question!
      ..then =>> Input.save(inp)!
      ...then =>> SE(inp) ... 
        {
            ( if SE.find(inp) =>> Output.definition!
           (( if not SE.find(inp) && <inp.is_alpha> =>> Output.recomendation!
            ( else =>> Output.typo!
        }

      << loop

      if Promt.exit ==> Diabolous.end! 
     * 
"""
