# AKA Port Studio
2
 
3
## Objectif
4
 
5
AKA Port Studio est un framework et un ensemble d'outils destinés à convertir des jeux Pokitto vers la console Gamebuino AKA.
6
 
7
Le projet privilégie :
8
 
9
- la conservation du code métier original ;
10
- le respect des auteurs ;
11
- le respect des licences ;
12
- l'automatisation maximale du portage ;
13
- l'intégration des standards de la plateforme AKA.
14
 
15
L'objectif n'est pas d'émuler la Pokitto mais de produire des applications AKA natives à partir des sources Pokitto.
16
 
17
---
18
 
19
# Architecture générale
20
 
21
```text
22
Projet Pokitto
23
│
24
▼
25
pokitto2aka
26
│
27
▼
28
Projet AKA
29
│
30
├── aka_runtime
31
├── pokitto_compat
32
└── code converti
33
│
34
▼
35
Compilation ESP-IDF
36
│
37
▼
38
Application AKA
39
```
40
 
41
---
42
 
43
# Composants
44
 
45
## aka_runtime
46
 
47
Composant système partagé par tous les ports.
48
 
49
### Responsabilités
50
 
51
- Menu système
52
- Gestion du volume
53
- Gestion des langues
54
- Captures d'écran
55
- Retour au loader
56
- Gestion de la carte SD
57
- Lecture du manifest
58
- Écran informations
59
- Écran crédits
60
- Écran licence
61
 
62
### API cible
63
 
64
```cpp
65
akaRuntime.begin();
66
akaRuntime.update();
67
 
68
akaRuntime.gamePath();
69
akaRuntime.settingsPath();
70
akaRuntime.screenshotPath();
71
 
72
akaRuntime.takeScreenshot();
73
akaRuntime.returnToLoader();
74
```
75
 
76
---
77
 
78
## pokitto_compat
79
 
80
Couche de compatibilité source Pokitto.
81
 
82
### Objectif
83
 
84
Permettre le remplacement :
85
 
86
```cpp
87
#include <Pokitto.h>
88
```
89
 
90
par :
91
 
92
```cpp
93
#include <pokitto_compat/Pokitto.h>
94
```
95
 
96
avec un minimum de modifications du code original.
97
 
98
### Périmètre V0.1
99
 
100
```cpp
101
Pokitto::Core
102
Pokitto::Display
103
Pokitto::Buttons
104
Pokitto::Sound
105
Pokitto::Cookie
106
Sprites
107
```
108
 
109
---
110
 
111
## compatibility_db
112
 
113
Base de connaissance décrivant l'état de compatibilité des API Pokitto.
114
 
115
### Exemple
116
 
117
```json
118
{
119
"Pokitto::Core::begin": {
120
"status": "supported"
121
},
122
 
123
"Pokitto::Display::drawBitmap": {
124
"status": "supported"
125
},
126
 
127
"Sprites::drawPlusMask": {
128
"status": "partial"
129
},
130
 
131
"Pokitto::Sound::playMusicStream": {
132
"status": "manual"
133
}
134
}
135
```
136
 
137
### Utilisation
138
 
139
- Analyseur
140
- Convertisseur
141
- Générateur de rapports
142
- Documentation
143
 
144
---
145
 
146
## pokitto2aka
147
 
148
Convertisseur principal.
149
 
150
### Fonctions
151
 
152
- Analyse du code source
153
- Détection des API Pokitto utilisées
154
- Extraction des métadonnées
155
- Extraction des licences
156
- Extraction des auteurs
157
- Conversion des assets
158
- Réécriture automatique
159
- Génération du projet AKA
160
- Génération du manifest
161
- Génération du rapport de compatibilité
162
 
163
### Exemple
164
 
165
```bash
166
pokitto2aka Kong-II-Pokitto/
167
```
168
 
169
---
170
 
171
# Runtime standard AKA
172
 
173
Tous les ports disposent automatiquement des fonctionnalités suivantes.
174
 
175
## MENU (appui court)
176
 
177
```text
178
Reprendre
179
 
180
Volume
181
 
182
Langue
183
 
184
Informations
185
 
186
Crédits
187
 
188
Licence
189
 
190
Retour Loader
191
```
192
 
193
---
194
 
195
## MENU (appui long)
196
 
197
```text
198
Capture écran
199
```
200
 
201
Capture enregistrée dans :
202
 
203
```text
204
/sdcard/AKA/screenshots/
205
```
206
 
207
---
208
 
209
## RUN + MENU (appui long)
210
 
211
```text
212
Retour Loader
213
```
214
 
215
---
216
 
217
# Stockage
218
 
219
## Répertoire système AKA
220
 
221
```text
222
/sdcard/AKA/
223
```
224
 
225
Contient :
226
 
227
```text
228
settings.json
229
screenshots/
230
lang/
231
```
232
 
233
---
234
 
235
## Répertoire du jeu
236
 
237
Exemple :
238
 
239
```text
240
/sdcard/kong2/
241
```
242
 
243
Contient :
244
 
245
```text
246
save.dat
247
config.json
248
highscores.dat
249
replay.dat
250
mods/
251
```
252
 
253
Le nom du répertoire est dérivé du champ `id` du manifest.
254
 
255
---
256
 
257
# Paramètres globaux
258
 
259
Fichier :
260
 
261
```text
262
/sdcard/AKA/settings.json
263
```
264
 
265
Exemple :
266
 
267
```json
268
{
269
"language": "fr",
270
"music_volume": 80,
271
"sfx_volume": 70
272
}
273
```
274
 
275
---
276
 
277
# Manifest
278
 
279
Chaque jeu converti possède un fichier de description.
280
 
281
Exemple :
282
 
283
```json
284
{
285
"id": "kong2",
286
 
287
"title": "Kong II",
288
 
289
"platform": "Pokitto",
290
 
291
"author": "Press Play On Tape",
292
 
293
"porter": "AKA Port Studio",
294
 
295
"license": "BSD-3-Clause",
296
 
297
"source_repository":
298
"https://github.com/Press-Play-On-Tape/Kong-II-Pokitto",
299
 
300
"supports_save": true,
301
"supports_screenshot": true,
302
"supports_languages": true,
303
 
304
"version": "1.0"
305
}
306
```
307
 
308
---
309
 
310
# Respect des auteurs
311
 
312
Chaque port doit obligatoirement afficher :
313
 
314
- Auteur original
315
- Licence originale
316
- Dépôt source original
317
- Auteur du portage
318
 
319
Ces informations sont accessibles depuis les écrans :
320
 
321
- Informations
322
- Crédits
323
- Licence
324
 
325
---
326
 
327
# Jeux de validation
328
 
329
## V0.1
330
 
331
- Kong-II
332
 
333
## V0.2
334
 
335
- Trials Of Astarok
336
- Galaxy Fighter
337
 
338
Chaque nouveau port devient un cas de test de régression permanent.
339
 
340
---
341
 
342
# Feuille de route
343
 
344
## V0.1
345
 
346
- aka_runtime
347
- pokitto_compat minimal
348
- compatibility_db
349
- analyseur
350
- convertisseur basique
351
- portage de Kong-II
352
 
353
## V0.2
354
 
355
- audio avancé
356
- support tilemaps
357
- assistant graphique
358
- amélioration de la conversion
359
 
360
## V1.0
361
 
362
Conversion automatisée :
363
 
364
```text
365
URL GitHub
366
↓
367
Analyse
368
↓
369
Conversion
370
↓
371
Compilation
372
↓
373
Projet AKA compilable
374
```
