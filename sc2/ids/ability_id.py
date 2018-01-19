# DO NOT EDIT!
# This file was automatically generated by "generate_id_constants.py"

import enum

class AbilityId(enum.Enum):
    INVALID = 0
    SMART = 1
    STOP_STOP = 4
    STOP_CHEER = 6
    STOP_DANCE = 7
    MOVE = 16
    PATROL = 17
    HOLDPOSITION = 18
    SCAN_MOVE = 19
    ATTACK_ATTACK = 23
    SPRAY_TERRAN = 26
    EFFECT_SPRAY_TERRAN = 26
    SPRAY_ZERG = 28
    EFFECT_SPRAY_ZERG = 28
    SPRAY_PROTOSS = 30
    EFFECT_SPRAY_PROTOSS = 30
    SALVAGE = 32
    EFFECT_SALVAGE = 32
    BEHAVIOR_HOLDFIREON_GHOST = 36
    EXPLODE = 42
    EFFECT_EXPLODE = 42
    RESEARCH_INTERCEPTORGRAVITONCATAPULT = 44
    RESEARCH_PHOENIXANIONPULSECRYSTALS = 46
    FUNGALGROWTH = 74
    EFFECT_FUNGALGROWTH = 74
    GUARDIANSHIELD = 76
    EFFECT_GUARDIANSHIELD = 76
    REPAIR_MULE = 78
    EFFECT_REPAIR_MULE = 78
    TRAIN_BANELING = 80
    TRAIN_MOTHERSHIP = 110
    FEEDBACK = 140
    EFFECT_FEEDBACK = 140
    POINTDEFENSEDRONE = 144
    EFFECT_POINTDEFENSEDRONE = 144
    HALLUCINATION_ARCHON = 146
    HALLUCINATION_COLOSSUS = 148
    HALLUCINATION_HIGHTEMPLAR = 150
    HALLUCINATION_IMMORTAL = 152
    HALLUCINATION_PHOENIX = 154
    HALLUCINATION_PROBE = 156
    HALLUCINATION_STALKER = 158
    HALLUCINATION_VOIDRAY = 160
    HALLUCINATION_WARPPRISM = 162
    HALLUCINATION_ZEALOT = 164
    HARVEST_RETURN_MULE = 167
    HUNTERSEEKERMISSILE = 169
    EFFECT_HUNTERSEEKERMISSILE = 169
    CALLDOWNMULE = 171
    EFFECT_CALLDOWNMULE = 171
    GRAVITONBEAM = 173
    EFFECT_GRAVITONBEAM = 173
    CANCEL_GRAVITONBEAM = 174
    SPAWNCHANGELING = 181
    EFFECT_SPAWNCHANGELING = 181
    RALLY_BUILDING = 195
    RALLY_MORPHING_UNIT = 199
    RALLY_COMMANDCENTER = 203
    RALLY_NEXUS = 207
    RALLY_HATCHERY_WORKERS = 211
    RALLY_HATCHERY_UNITS = 212
    RESEARCH_GLIALREGENERATION = 216
    RESEARCH_TUNNELINGCLAWS = 217
    INFESTEDTERRANS = 247
    EFFECT_INFESTEDTERRANS = 247
    NEURALPARASITE = 249
    EFFECT_NEURALPARASITE = 249
    INJECTLARVA = 251
    EFFECT_INJECTLARVA = 251
    STIM_MARAUDER = 253
    EFFECT_STIM_MARAUDER = 253
    SUPPLYDROP = 255
    EFFECT_SUPPLYDROP = 255
    CHRONOBOOST = 261
    EFFECT_CHRONOBOOST = 261
    RESEARCH_CHITINOUSPLATING = 265
    HARVEST_GATHER_SCV = 295
    HARVEST_RETURN_SCV = 296
    HARVEST_GATHER_PROBE = 298
    HARVEST_RETURN_PROBE = 299
    CANCEL_QUEUE1 = 304
    CANCELSLOT_QUEUE1 = 305
    CANCEL_QUEUE5 = 306
    CANCELSLOT_QUEUE5 = 307
    CANCEL_QUEUECANCELTOSELECTION = 308
    CANCELSLOT_QUEUECANCELTOSELECTION = 309
    CANCEL_QUEUEADDON = 312
    CANCELSLOT_ADDON = 313
    CANCEL_BUILDINPROGRESS = 314
    HALT_BUILDING = 315
    REPAIR_SCV = 316
    EFFECT_REPAIR_SCV = 316
    BUILD_COMMANDCENTER = 318
    BUILD_SUPPLYDEPOT = 319
    BUILD_REFINERY = 320
    BUILD_BARRACKS = 321
    BUILD_ENGINEERINGBAY = 322
    BUILD_MISSILETURRET = 323
    BUILD_BUNKER = 324
    BUILD_SENSORTOWER = 326
    BUILD_GHOSTACADEMY = 327
    BUILD_FACTORY = 328
    BUILD_STARPORT = 329
    BUILD_ARMORY = 331
    BUILD_FUSIONCORE = 333
    HALT_TERRANBUILD = 348
    STIM_MARINE = 380
    EFFECT_STIM_MARINE = 380
    BEHAVIOR_CLOAKON_GHOST = 382
    BEHAVIOR_CLOAKOFF_GHOST = 383
    HEAL = 386
    EFFECT_HEAL = 386
    MORPH_SIEGEMODE = 388
    MORPH_UNSIEGE = 390
    BEHAVIOR_CLOAKON_BANSHEE = 392
    BEHAVIOR_CLOAKOFF_BANSHEE = 393
    LOAD_MEDIVAC = 394
    UNLOADALLAT_MEDIVAC = 396
    UNLOADUNIT_MEDIVAC = 397
    SCAN = 399
    EFFECT_SCAN = 399
    YAMATOGUN = 401
    EFFECT_YAMATOGUN = 401
    MORPH_VIKINGASSAULTMODE = 403
    MORPH_VIKINGFIGHTERMODE = 405
    LOAD_BUNKER = 407
    UNLOADALL_BUNKER = 408
    UNLOADUNIT_BUNKER = 410
    UNLOADALL_COMMANDCENTER = 413
    UNLOADUNIT_COMMANDCENTER = 415
    LOADALL_COMMANDCENTER = 416
    LIFT_COMMANDCENTER = 417
    LAND_COMMANDCENTER = 419
    BUILD_TECHLAB_BARRACKS = 421
    BUILD_REACTOR_BARRACKS = 422
    CANCEL_BARRACKSADDON = 451
    LIFT_BARRACKS = 452
    BUILD_TECHLAB_FACTORY = 454
    BUILD_REACTOR_FACTORY = 455
    CANCEL_FACTORYADDON = 484
    LIFT_FACTORY = 485
    BUILD_TECHLAB_STARPORT = 487
    BUILD_REACTOR_STARPORT = 488
    CANCEL_STARPORTADDON = 517
    LIFT_STARPORT = 518
    LAND_FACTORY = 520
    LAND_STARPORT = 522
    TRAIN_SCV = 524
    LAND_BARRACKS = 554
    MORPH_SUPPLYDEPOT_LOWER = 556
    MORPH_SUPPLYDEPOT_RAISE = 558
    TRAIN_MARINE = 560
    TRAIN_REAPER = 561
    TRAIN_GHOST = 562
    TRAIN_MARAUDER = 563
    TRAIN_SIEGETANK = 591
    TRAIN_THOR = 594
    TRAIN_HELLION = 595
    TRAIN_HELLBAT = 596
    TRAIN_CYCLONE = 597
    TRAIN_WIDOWMINE = 614
    TRAIN_MEDIVAC = 620
    TRAIN_BANSHEE = 621
    TRAIN_RAVEN = 622
    TRAIN_BATTLECRUISER = 623
    TRAIN_VIKINGFIGHTER = 624
    TRAIN_LIBERATOR = 626
    RESEARCH_HISECAUTOTRACKING = 650
    RESEARCH_TERRANSTRUCTUREARMORUPGRADE = 651
    RESEARCH_TERRANINFANTRYWEAPONSLEVEL1 = 652
    RESEARCH_TERRANINFANTRYWEAPONSLEVEL2 = 653
    RESEARCH_TERRANINFANTRYWEAPONSLEVEL3 = 654
    RESEARCH_NEOSTEELFRAME = 655
    RESEARCH_TERRANINFANTRYARMORLEVEL1 = 656
    RESEARCH_TERRANINFANTRYARMORLEVEL2 = 657
    RESEARCH_TERRANINFANTRYARMORLEVEL3 = 658
    BUILD_NUKE = 710
    RESEARCH_STIMPACK = 730
    RESEARCH_COMBATSHIELD = 731
    RESEARCH_CONCUSSIVESHELLS = 732
    RESEARCH_INFERNALPREIGNITER = 761
    RESEARCH_DRILLINGCLAWS = 764
    RESEARCH_MAGFIELDLAUNCHERS = 766
    RESEARCH_SMARTSERVOS = 766
    RESEARCH_RAPIDFIRELAUNCHERS = 768
    RESEARCH_BANSHEECLOAKINGFIELD = 790
    RESEARCH_RAVENCORVIDREACTOR = 793
    RESEARCH_BANSHEEHYPERFLIGHTROTORS = 799
    RESEARCH_RAVENRECALIBRATEDEXPLOSIVES = 803
    RESEARCH_HIGHCAPACITYFUELTANKS = 804
    RESEARCH_ADVANCEDBALLISTICS = 805
    RESEARCH_ENHANCEDMUNITIONS = 806
    RESEARCH_PERSONALCLOAKING = 820
    RESEARCH_TERRANVEHICLEWEAPONSLEVEL1 = 855
    RESEARCH_TERRANVEHICLEWEAPONSLEVEL2 = 856
    RESEARCH_TERRANVEHICLEWEAPONSLEVEL3 = 857
    RESEARCH_TERRANSHIPWEAPONSLEVEL1 = 861
    RESEARCH_TERRANSHIPWEAPONSLEVEL2 = 862
    RESEARCH_TERRANSHIPWEAPONSLEVEL3 = 863
    RESEARCH_TERRANVEHICLEANDSHIPPLATINGLEVEL1 = 864
    RESEARCH_TERRANVEHICLEANDSHIPPLATINGLEVEL2 = 865
    RESEARCH_TERRANVEHICLEANDSHIPPLATINGLEVEL3 = 866
    BUILD_NEXUS = 880
    BUILD_PYLON = 881
    BUILD_ASSIMILATOR = 882
    BUILD_GATEWAY = 883
    BUILD_FORGE = 884
    BUILD_FLEETBEACON = 885
    BUILD_TWILIGHTCOUNCIL = 886
    BUILD_PHOTONCANNON = 887
    BUILD_STARGATE = 889
    BUILD_TEMPLARARCHIVE = 890
    BUILD_DARKSHRINE = 891
    BUILD_ROBOTICSBAY = 892
    BUILD_ROBOTICSFACILITY = 893
    BUILD_CYBERNETICSCORE = 894
    BUILD_SHIELDBATTERY = 895
    UNLOADALLAT_WARPPRISM = 913
    UNLOADUNIT_WARPPRISM = 914
    TRAIN_ZEALOT = 916
    TRAIN_STALKER = 917
    TRAIN_HIGHTEMPLAR = 919
    TRAIN_DARKTEMPLAR = 920
    TRAIN_SENTRY = 921
    TRAIN_ADEPT = 922
    TRAIN_PHOENIX = 946
    TRAIN_CARRIER = 948
    TRAIN_VOIDRAY = 950
    TRAIN_ORACLE = 954
    TRAIN_TEMPEST = 955
    TRAIN_WARPPRISM = 976
    TRAIN_OBSERVER = 977
    TRAIN_COLOSSUS = 978
    TRAIN_IMMORTAL = 979
    TRAIN_DISRUPTOR = 994
    TRAIN_PROBE = 1006
    PSISTORM = 1036
    EFFECT_PSISTORM = 1036
    BUILD_INTERCEPTORS = 1042
    RESEARCH_PROTOSSGROUNDWEAPONSLEVEL1 = 1062
    RESEARCH_PROTOSSGROUNDWEAPONSLEVEL2 = 1063
    RESEARCH_PROTOSSGROUNDWEAPONSLEVEL3 = 1064
    RESEARCH_PROTOSSGROUNDARMORLEVEL1 = 1065
    RESEARCH_PROTOSSGROUNDARMORLEVEL2 = 1066
    RESEARCH_PROTOSSGROUNDARMORLEVEL3 = 1067
    RESEARCH_PROTOSSSHIELDSLEVEL1 = 1068
    RESEARCH_PROTOSSSHIELDSLEVEL2 = 1069
    RESEARCH_PROTOSSSHIELDSLEVEL3 = 1070
    RESEARCH_GRAVITICBOOSTER = 1093
    RESEARCH_GRAVITICDRIVE = 1094
    RESEARCH_EXTENDEDTHERMALLANCE = 1097
    RESEARCH_PSISTORM = 1126
    BUILD_HATCHERY = 1152
    BUILD_EXTRACTOR = 1154
    BUILD_SPAWNINGPOOL = 1155
    BUILD_EVOLUTIONCHAMBER = 1156
    BUILD_HYDRALISKDEN = 1157
    BUILD_SPIRE = 1158
    BUILD_ULTRALISKCAVERN = 1159
    BUILD_INFESTATIONPIT = 1160
    BUILD_NYDUSNETWORK = 1161
    BUILD_BANELINGNEST = 1162
    BUILD_ROACHWARREN = 1165
    BUILD_SPINECRAWLER = 1166
    BUILD_SPORECRAWLER = 1167
    HARVEST_GATHER_DRONE = 1183
    HARVEST_RETURN_DRONE = 1184
    RESEARCH_ZERGMELEEWEAPONSLEVEL1 = 1186
    RESEARCH_ZERGMELEEWEAPONSLEVEL2 = 1187
    RESEARCH_ZERGMELEEWEAPONSLEVEL3 = 1188
    RESEARCH_ZERGGROUNDARMORLEVEL1 = 1189
    RESEARCH_ZERGGROUNDARMORLEVEL2 = 1190
    RESEARCH_ZERGGROUNDARMORLEVEL3 = 1191
    RESEARCH_ZERGMISSILEWEAPONSLEVEL1 = 1192
    RESEARCH_ZERGMISSILEWEAPONSLEVEL2 = 1193
    RESEARCH_ZERGMISSILEWEAPONSLEVEL3 = 1194
    MORPH_LAIR = 1216
    CANCEL_MORPHLAIR = 1217
    MORPH_HIVE = 1218
    MORPH_GREATERSPIRE = 1220
    RESEARCH_PNEUMATIZEDCARAPACE = 1223
    RESEARCH_BURROW = 1225
    RESEARCH_ZERGLINGADRENALGLANDS = 1252
    RESEARCH_ZERGLINGMETABOLICBOOST = 1253
    RESEARCH_GROOVEDSPINES = 1282
    RESEARCH_MUSCULARAUGMENTS = 1283
    RESEARCH_ZERGFLYERATTACKLEVEL1 = 1312
    RESEARCH_ZERGFLYERATTACKLEVEL2 = 1313
    RESEARCH_ZERGFLYERATTACKLEVEL3 = 1314
    RESEARCH_ZERGFLYERARMORLEVEL1 = 1315
    RESEARCH_ZERGFLYERARMORLEVEL2 = 1316
    RESEARCH_ZERGFLYERARMORLEVEL3 = 1317
    TRAIN_DRONE = 1342
    TRAIN_ZERGLING = 1343
    TRAIN_OVERLORD = 1344
    TRAIN_HYDRALISK = 1345
    TRAIN_MUTALISK = 1346
    TRAIN_ULTRALISK = 1348
    TRAIN_ROACH = 1351
    TRAIN_INFESTOR = 1352
    TRAIN_CORRUPTOR = 1353
    TRAIN_VIPER = 1354
    TRAIN_SWARMHOST = 1356
    MORPH_BROODLORD = 1372
    CANCEL_MORPHBROODLORD = 1373
    BURROWDOWN_BANELING = 1374
    BURROWUP_BANELING = 1376
    BURROWDOWN_DRONE = 1378
    BURROWUP_DRONE = 1380
    BURROWDOWN_HYDRALISK = 1382
    BURROWUP_HYDRALISK = 1384
    BURROWDOWN_ROACH = 1386
    BURROWUP_ROACH = 1388
    BURROWDOWN_ZERGLING = 1390
    BURROWUP_ZERGLING = 1392
    UNLOADALLAT_OVERLORD = 1408
    UNLOADUNIT_OVERLORD = 1409
    TRAINWARP_ZEALOT = 1413
    TRAINWARP_STALKER = 1414
    TRAINWARP_HIGHTEMPLAR = 1416
    TRAINWARP_DARKTEMPLAR = 1417
    TRAINWARP_SENTRY = 1418
    TRAINWARP_ADEPT = 1419
    BURROWDOWN_QUEEN = 1433
    BURROWUP_QUEEN = 1435
    UNLOADALL_NYDASNETWORK = 1438
    UNLOADUNIT_NYDASNETWORK = 1440
    BLINK_STALKER = 1442
    EFFECT_BLINK_STALKER = 1442
    BURROWDOWN_INFESTOR = 1444
    BURROWUP_INFESTOR = 1446
    MORPH_OVERSEER = 1448
    CANCEL_MORPHOVERSEER = 1449
    MORPH_PLANETARYFORTRESS = 1450
    CANCEL_MORPHPLANETARYFORTRESS = 1451
    RESEARCH_PATHOGENGLANDS = 1454
    RESEARCH_NEURALPARASITE = 1455
    RESEARCH_CENTRIFUGALHOOKS = 1482
    MORPH_ORBITALCOMMAND = 1516
    CANCEL_MORPHORBITAL = 1517
    MORPH_WARPGATE = 1518
    MORPH_GATEWAY = 1520
    LIFT_ORBITALCOMMAND = 1522
    LAND_ORBITALCOMMAND = 1524
    FORCEFIELD = 1526
    EFFECT_FORCEFIELD = 1526
    MORPH_WARPPRISMPHASINGMODE = 1528
    MORPH_WARPPRISMTRANSPORTMODE = 1530
    RESEARCH_BATTLECRUISERWEAPONREFIT = 1532
    RESEARCH_PROTOSSAIRWEAPONSLEVEL1 = 1562
    RESEARCH_PROTOSSAIRWEAPONSLEVEL2 = 1563
    RESEARCH_PROTOSSAIRWEAPONSLEVEL3 = 1564
    RESEARCH_PROTOSSAIRARMORLEVEL1 = 1565
    RESEARCH_PROTOSSAIRARMORLEVEL2 = 1566
    RESEARCH_PROTOSSAIRARMORLEVEL3 = 1567
    RESEARCH_WARPGATE = 1568
    RESEARCH_CHARGE = 1592
    RESEARCH_BLINK = 1593
    RESEARCH_ADEPTRESONATINGGLAIVES = 1594
    NUKECALLDOWN = 1622
    EFFECT_NUKECALLDOWN = 1622
    EMP = 1628
    EFFECT_EMP = 1628
    TRAIN_QUEEN = 1632
    TRANSFUSION = 1664
    EFFECT_TRANSFUSION = 1664
    ATTACK_REDIRECT = 1682
    STIM_MARINE_REDIRECT = 1683
    EFFECT_STIM_MARINE_REDIRECT = 1683
    STOP_REDIRECT = 1691
    BEHAVIOR_GENERATECREEPON = 1692
    BEHAVIOR_GENERATECREEPOFF = 1693
    BUILD_CREEPTUMOR_QUEEN = 1694
    MORPH_SPINECRAWLERUPROOT = 1725
    MORPH_SPORECRAWLERUPROOT = 1727
    MORPH_SPINECRAWLERROOT = 1729
    CANCEL_SPINECRAWLERROOT = 1730
    MORPH_SPORECRAWLERROOT = 1731
    BUILD_CREEPTUMOR_TUMOR = 1733
    CANCEL_CREEPTUMOR = 1763
    AUTOTURRET = 1764
    EFFECT_AUTOTURRET = 1764
    MORPH_ARCHON = 1766
    BUILD_NYDUSWORM = 1768
    CHARGE = 1819
    EFFECT_CHARGE = 1819
    CONTAMINATE = 1825
    EFFECT_CONTAMINATE = 1825
    CANCEL_QUEUEPASIVE = 1831
    CANCELSLOT_QUEUEPASSIVE = 1832
    CANCEL_QUEUEPASSIVECANCELTOSELECTION = 1833
    MORPH_MOTHERSHIP = 1847
    CANCEL_MORPHMOTHERSHIP = 1848
    TRAIN_MOTHERSHIPCORE = 1853
    MASSRECALL_MOTHERSHIPCORE = 1974
    EFFECT_MASSRECALL_MOTHERSHIPCORE = 1974
    MORPH_HELLION = 1978
    MORPH_HELLBAT = 1998
    BURROWDOWN_SWARMHOST = 2014
    BURROWUP_SWARMHOST = 2016
    ATTACK_ATTACKBUILDING = 2048
    STOP_BUILDING = 2057
    BLINDINGCLOUD = 2063
    EFFECT_BLINDINGCLOUD = 2063
    ABDUCT = 2067
    EFFECT_ABDUCT = 2067
    VIPERCONSUME = 2073
    EFFECT_VIPERCONSUME = 2073
    BEHAVIOR_BUILDINGATTACKON = 2081
    BEHAVIOR_BUILDINGATTACKOFF = 2082
    BURROWDOWN_WIDOWMINE = 2095
    BURROWUP_WIDOWMINE = 2097
    WIDOWMINEATTACK = 2099
    EFFECT_WIDOWMINEATTACK = 2099
    BURROWDOWN_LURKER = 2108
    BURROWUP_LURKER = 2110
    MORPH_LURKERDEN = 2112
    CANCEL_MORPHLURKERDEN = 2113
    HALLUCINATION_ORACLE = 2114
    MEDIVACIGNITEAFTERBURNERS = 2116
    EFFECT_MEDIVACIGNITEAFTERBURNERS = 2116
    ORACLEREVELATION = 2146
    EFFECT_ORACLEREVELATION = 2146
    PHOTONOVERCHARGE = 2162
    EFFECT_PHOTONOVERCHARGE = 2162
    TIMEWARP = 2244
    EFFECT_TIMEWARP = 2244
    CAUSTICSPRAY = 2324
    EFFECT_CAUSTICSPRAY = 2324
    IMMORTALBARRIER = 2328
    EFFECT_IMMORTALBARRIER = 2328
    MORPH_RAVAGER = 2330
    CANCEL_MORPHRAVAGER = 2331
    MORPH_LURKER = 2332
    CANCEL_MORPHLURKER = 2333
    CORROSIVEBILE = 2338
    EFFECT_CORROSIVEBILE = 2338
    BURROWDOWN_RAVAGER = 2340
    BURROWUP_RAVAGER = 2342
    PURIFICATIONNOVA = 2346
    EFFECT_PURIFICATIONNOVA = 2346
    LOCKON = 2350
    EFFECT_LOCKON = 2350
    TACTICALJUMP = 2358
    EFFECT_TACTICALJUMP = 2358
    MORPH_THORHIGHIMPACTMODE = 2362
    MORPH_THOREXPLOSIVEMODE = 2364
    MASSRECALL_MOTHERSHIP = 2368
    EFFECT_MASSRECALL_MOTHERSHIP = 2368
    UNLOADALL_NYDUSWORM = 2371
    BEHAVIOR_PULSARBEAMON = 2375
    BEHAVIOR_PULSARBEAMOFF = 2376
    LOCUSTSWOOP = 2387
    EFFECT_LOCUSTSWOOP = 2387
    HALLUCINATION_DISRUPTOR = 2389
    HALLUCINATION_ADEPT = 2391
    VOIDRAYPRISMATICALIGNMENT = 2393
    EFFECT_VOIDRAYPRISMATICALIGNMENT = 2393
    BUILD_STASISTRAP = 2505
    PARASITICBOMB = 2542
    EFFECT_PARASITICBOMB = 2542
    ADEPTPHASESHIFT = 2544
    EFFECT_ADEPTPHASESHIFT = 2544
    BEHAVIOR_HOLDFIREON_LURKER = 2550
    BEHAVIOR_HOLDFIREOFF_LURKER = 2552
    MORPH_LIBERATORAGMODE = 2558
    MORPH_LIBERATORAAMODE = 2560
    KD8CHARGE = 2588
    EFFECT_KD8CHARGE = 2588
    CANCEL_ADEPTPHASESHIFT = 2594
    CANCEL_ADEPTSHADEPHASESHIFT = 2596
    TEMPESTDISRUPTIONBLAST = 2698
    EFFECT_TEMPESTDISRUPTIONBLAST = 2698
    SHADOWSTRIDE = 2700
    EFFECT_SHADOWSTRIDE = 2700
    SPAWNLOCUSTS = 2704
    EFFECT_SPAWNLOCUSTS = 2704
    MORPH_OVERLORDTRANSPORT = 2708
    CANCEL_MORPHOVERLORDTRANSPORT = 2709
    GHOSTSNIPE = 2714
    EFFECT_GHOSTSNIPE = 2714
    RESEARCH_SHADOWSTRIKE = 2720
    CANCEL = 3659
    HALT = 3660
    BURROWDOWN = 3661
    BURROWUP = 3662
    LOADALL = 3663
    UNLOADALL = 3664
    STOP = 3665
    HARVEST_GATHER = 3666
    HARVEST_RETURN = 3667
    LOAD = 3668
    UNLOADALLAT = 3669
    CANCEL_LAST = 3671
    RALLY_UNITS = 3673
    ATTACK = 3674
    STIM = 3675
    EFFECT_STIM = 3675
    BEHAVIOR_CLOAKON = 3676
    BEHAVIOR_CLOAKOFF = 3677
    LAND = 3678
    LIFT = 3679
    MORPH_ROOT = 3680
    MORPH_UPROOT = 3681
    BUILD_TECHLAB = 3682
    BUILD_REACTOR = 3683
    SPRAY = 3684
    EFFECT_SPRAY = 3684
    REPAIR = 3685
    EFFECT_REPAIR = 3685
    MASSRECALL = 3686
    EFFECT_MASSRECALL = 3686
    BLINK = 3687
    EFFECT_BLINK = 3687
    BEHAVIOR_HOLDFIREON = 3688
    BEHAVIOR_HOLDFIREOFF = 3689
    RALLY_WORKERS = 3690
    BUILD_CREEPTUMOR = 3691
    RESEARCH_PROTOSSAIRARMOR = 3692
    RESEARCH_PROTOSSAIRWEAPONS = 3693
    RESEARCH_PROTOSSGROUNDARMOR = 3694
    RESEARCH_PROTOSSGROUNDWEAPONS = 3695
    RESEARCH_PROTOSSSHIELDS = 3696
    RESEARCH_TERRANINFANTRYARMOR = 3697
    RESEARCH_TERRANINFANTRYWEAPONS = 3698
    RESEARCH_TERRANSHIPWEAPONS = 3699
    RESEARCH_TERRANVEHICLEANDSHIPPLATING = 3700
    RESEARCH_TERRANVEHICLEWEAPONS = 3701
    RESEARCH_ZERGFLYERARMOR = 3702
    RESEARCH_ZERGFLYERATTACK = 3703
    RESEARCH_ZERGGROUNDARMOR = 3704
    RESEARCH_ZERGMELEEWEAPONS = 3705
    RESEARCH_ZERGMISSILEWEAPONS = 3706
    RESTORE = 3765
    EFFECT_RESTORE = 3765

for item in AbilityId:
    globals()[item.name] = item
