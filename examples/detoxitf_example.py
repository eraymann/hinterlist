# coding=utf-8
import json

from hinterlist import detox

skeleton = detox.get_skeleton(in_file=r"D:\temp\0021.xtf")
print(json.dumps(skeleton, indent=4, sort_keys=True))

# detoxitf.remove_unused_tables(
#     in_itf=r"D:\temp\0001.itf",
#     out_itf=r"D:\temp\0001_clean.itf",
#     keep={
#         "Bodenbedeckung": [
#             "BoFlaeche",
#             "BoFlaeche_Geometrie",
#             "Gebaeudenummer",
#             "Objektname",
#             "ProjBoFlaeche",
#             "ProjBoFlaeche_Geometrie",
#             "ProjGebaeudenummer",
#             "ProjObjektname",
#         ],
#         "Einzelobjekte": [
#             "Einzelobjekt",
#             "Flaechenelement",
#             "Flaechenelement_Geometrie",
#             "Objektname",
#             "Objektnummer"
#         ],
#         "Gebaeudeadressen": [
#             "Lokalisation",
#             "LokalisationsName",
#             "LokalisationsNamePos",
#             "BenanntesGebiet",
#             "BenanntesGebiet_Flaeche",
#             "Strassenstueck",
#             "Gebaeudeeingang",
#         ],
#         "Liegenschaften": [
#             "ProjGrundstueck",
#             "ProjLiegenschaft",
#             "ProjLiegenschaft_Geometrie",
#             "Grundstueck",
#             "Liegenschaft_Geometrie",
#             "Liegenschaft"
#         ]
#     }
# )
