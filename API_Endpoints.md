Creiamo un'applicazione web per il fantacalcio usando python come backend e streamlit come frontend.
L'applicazione deve permettere agli utenti di analizzare le statistiche dei giocatori di calcio e di creare la propria squadra ideale.

Per rilevare i dati dei calciatori utilizziamo le API di sofascore

L'elenco delle squadre è rilevabile tramite l'endpoint:
https://www.sofascore.com/api/v1/unique-tournament/23/season/76457/standings/total

il risultato è un json del tipo:
{
standings: [
{
type: "total",
descriptions: [ ],
tieBreakingRule: {
text: "In the event that two (or more) teams have an equal number of points, the following rules break the tie:

1. Head-to-head if all tied teams have paired matches
2. Goal difference
3. Goals scored",
id: 1239
},
rows: [
{
team: {
name: "Milan",
slug: "milan",
shortName: "Milan",
gender: "M",
sport: {
name: "Football",
slug: "football",
id: 1
},
userCount: 1718910,
nameCode: "MIL",
disabled: false,
national: false,
type: 0,
id: 2692,
country: {
alpha2: "IT",
alpha3: "ITA",
name: "Italy",
slug: "italy"
},
teamColors: {
primary: "#000000",
secondary: "#cc0000",
text: "#cc0000"
},
fieldTranslations: {
nameTranslation: {
ar: "ميلان",
ru: "Милан",
hi: "मिलान",
bn: "মিলান"
},
shortNameTranslation: { }
}
},
descriptions: [ ],
promotion: {
text: "Champions League",
id: 804
...


standings.rows.team.id è l'id della squadra che ci serve per rilevare i giocatori

I giocatori di ogni squadra sono rilevabili tramite l'endpoint:

https://www.sofascore.com/api/v1/team/id/players


il risultato è del tipo:

{
players: [
{
player: {
name: "Edin Džeko",
firstName: "",
lastName: "",
slug: "edin-dzeko",
shortName: "E. Džeko",
team: {},
position: "F",
positionsDetailed: [],
jerseyNumber: "11",
height: 193,
dateOfBirth: "1986-03-17T00:00:00+00:00",
preferredFoot: "Both",
userCount: 23552,
gender: "M",
sofascoreId: "EDzeko",
id: 14990,
country: {},
shirtNumber: 11,
dateOfBirthTimestamp: 511401600,
contractUntilTimestamp: 1782777600,
proposedMarketValue: 1400000,
proposedMarketValueRaw: {
value: 1400000,
currency: "EUR"
},
fieldTranslations: {
nameTranslation: {
ar: "إدين دزيكو",
hi: "एडिन जेको",
bn: "এডিন জেকো"
},
shortNameTranslation: {
ar: "إ. دزيكو",
hi: "ई. जेको",
bn: "ই. জেকো"
}
}
}
},
{
player: {
name: "Moise Kean",
firstName: "",
lastName: "",
slug: "moise-kean",

Per accedere alle statistiche serve il campo id del giocatore rilevabile in players.player.id

L'endpoint per le statistiche è:
https://www.sofascore.com/api/v1/player/id/statistics


Il risultato è del tipo:

{
seasons: [
{
statistics: {
accuratePasses: 10,
accuratePassesPercentage: 100,
assists: 1,
bigChancesCreated: 1,
bigChancesMissed: 0,
blockedShots: 0,
cleanSheet: 0,
dribbledPast: 0,
errorLeadToGoal: 0,
goals: 0,
goalsAssistsSum: 1,
goalsConceded: 0,
interceptions: 0,
keyPasses: 1,
minutesPlayed: 74,
passToAssist: 0,
rating: 6.9,
redCards: 0,
saves: 0,
shotsOnTarget: 0,
successfulDribbles: 1,
tackles: 1,
totalShots: 1,
yellowCards: 0,
totalRating: 6.9,
countRating: 1,
totalPasses: 10,
shotsFromInsideTheBox: 1,
appearances: 1,
type: "overall",
id: 0
},
year: "25/26",
startYear: 2025,
endYear: 2026,
team: {
name: "Milan",
slug: "milan",
shortName: "Milan",
gender: "M",
sport: {
name: "Football",
slug: "football",
id: 1
},
userCount: 1718910,
nameCode: "MIL",
disabled: false,
national: false,
type: 0,
id: 2692,
teamColors: {
primary: "#000000",
secondary: "#cc0000",
text: "#cc0000"
},
fieldTranslations: {
nameTranslation: {
ar: "ميلان",
ru: "Милан",
hi: "मिलान",
bn: "মিলান"
},
shortNameTranslation: { }
}
},
uniqueTournament: {
name: "Coppa Italia",
slug: "coppa-italia",
primaryColorHex: "#8d041e",
secondaryColorHex: "#bd0a1f",
category: {
name: "Italy",
slug: "italy",
sport: {
name: "Football",
slug: "football",
id: 1
},
id: 31,
flag: "italy",
alpha2: "IT",
fieldTranslations: {
nameTranslation: {
ar: "إيطاليا",
hi: "इटली",
bn: "ইতালি"
},
shortNameTranslation: { }
}
},
userCount: 101994,
id: 328,
displayInverseHomeAwayTeams: false,
fieldTranslations: {
nameTranslation: {
ar: "كأس إيطاليا",
hi: "कोपा इटालिया",
bn: "কোপা ইতালিয়া"
},
shortNameTranslation: { }
},
competitionType: "domestic-cup"
},
season: {
name: "Coppa Italia 25/26",
year: "25/26",
editor: false,
id: 77308
}
},
{
statistics: {
accurateLongBalls: 1,
accurateLongBallsPercentage: 50,
accuratePasses: 20,
accuratePassesPercentage: 62.5,
aerialDuelsWon: 2,
assists: 1,
bigChancesCreated: 1,
bigChancesMissed: 3,
blockedShots: 0,
cleanSheet: 0,
dribbledPast: 2,
errorLeadToGoal: 0,
goals: 0,
goalsAssistsSum: 1,
goalsConceded: 2,
interceptions: 0,
keyPasses: 1,
minutesPlayed: 175,
passToAssist: 0,
rating: 6.42,
redCards: 0,
saves: 0,
shotsOnTarget: 3,
successfulDribbles: 1,
tackles: 0,
totalShots: 6,
yellowCards: 0,
totalRating: 38.5,
countRating: 6,
totalLongBalls: 2,
totalPasses: 32,
shotsFromInsideTheBox: 4,
appearances: 6,
type: "overall",
id: 0
},
year: "2025",
startYear: 2025,
endYear: 2025,
team: {
name: "Mexico",
slug: "mexico",
shortName: "Mexico",
gender: "M",
sport: {
name: "Football",
slug: "football",
id: 1
},
userCount: 262741,
nameCode: "MEX",
ranking: 13,
disabled: false,
national: true,
type: 0,
id: 4781,
teamColors: {
primary: "#1a4d3e",
secondary: "#960000",
text: "#960000"
},
fieldTranslations: {
nameTranslation: {
ar: "المكسيك",
ru: "Мексика",
hi: "मेक्सिको",
bn: "মেক্সিকো"
},
shortNameTranslation: { }
}
},
uniqueTournament: {
name: "CONCACAF Gold Cup",
slug: "concacaf-gold-cup",
primaryColorHex: "#031236",
secondaryColorHex: "#ffc84e",
category: {
name: "North & Central America",
slug: "north-central-america",
sport: {
name: "Football",
slug: "football",
id: 1
},
id: 1469,
flag: "north-and-central-america"
},
userCount: 46431,
id: 140,
displayInverseHomeAwayTeams: false,
fieldTranslations: {
nameTranslation: {
ar: "كأس الكونكاكاف الذهبي",
hi: "कोंकाकाफ गोल्ड कप",
bn: "কনকাক্যাফ গোল্ড কাপ"
},
shortNameTranslation: { }
},
competitionType: "national"
},
season: {
name: "CONCACAF Gold Cup 2025",
year: "2025",
editor: false,
id: 72840
}
},
{
statistics: {
accuratePasses: 15,
accuratePassesPercentage: 83.33,
aerialDuelsWon: 1,
assists: 0,
bigChancesCreated: 0,
bigChancesMissed: 2,
blockedShots: 0,
cleanSheet: 0,
dribbledPast: 0,
errorLeadToGoal: 0,
goals: 1,
goalsAssistsSum: 1,
goalsConceded: 3,
interceptions: 0,
keyPasses: 0,
minutesPlayed: 93,
passToAssist: 0,
rating: 6.4,
redCards: 0,
saves: 0,
shotsOnTarget: 2,
successfulDribbles: 0,
tackles: 0,
totalShots: 5,
yellowCards: 0,
totalRating: 12.8,
countRating: 2,
totalPasses: 18,
shotsFromInsideTheBox: 3,
appearances: 2,
type: "overall",
id: 0
},
year: "2025",
startYear: 2025,
endYear: 2025,
team: {
name: "Mexico",
slug: "mexico",
shortName: "Mexico",
gender: "M",
sport: {
name: "Football",
slug: "football",
id: 1
},
userCount: 262741,
nameCode: "MEX",
ranking: 13,
disabled: false,
national: true,
type: 0,
id: 4781,
teamColors: {
primary: "#1a4d3e",
secondary: "#960000",
text: "#960000"
},
fieldTranslations: {
nameTranslation: {
ar: "المكسيك",
ru: "Мексика",
hi: "मेक्सिको",
bn: "মেক্সিকো"
},
shortNameTranslation: { }
}
},
uniqueTournament: {
name: "International Friendly Games",
slug: "int-friendly-games",
primaryColorHex: "#25497d",
secondaryColorHex: "#d38f1d",
category: {
name: "World",
slug: "world",
sport: {
name: "Football",
slug: "football",
id: 1
},
id: 1468,
flag: "international",
fieldTranslations: {
nameTranslation: {
ar: "العالم",
hi: "विश्व",
bn: "বিশ্ব"
},
shortNameTranslation: { }
}
},
userCount: 75389,
id: 851,
displayInverseHomeAwayTeams: false,
fieldTranslations: {
nameTranslation: {
ar: "مباريات ودية دولية",
hi: "इंटरनेशनल फ्रेंडली गेम्स",
bn: "ইন্টারন্যাশনাল ফ্রেন্ডলি গেমস"
},
shortNameTranslation: { }
},
competitionType: "national"
},
season: {
name: "Int. Friendly Games 2025",
year: "2025",
editor: false,
id: 69578
}
},
{
statistics: {
accurateCrosses: 1,
accurateCrossesPercentage: 50,
accurateLongBalls: 0,
accurateLongBallsPercentage: 0,
accuratePasses: 76,
accuratePassesPercentage: 80.85,
aerialDuelsWon: 7,
assists: 2,
bigChancesCreated: 3,
bigChancesMissed: 4,
blockedShots: 1,
outfielderBlocks: 1,
cleanSheet: 0,
dribbledPast: 1,
errorLeadToGoal: 0,
expectedAssists: 0.45263229,
expectedGoals: 4.8378,
goals: 5,
goalsAssistsSum: 7,
goalsConceded: 9,
interceptions: 1,
keyPasses: 6,
minutesPlayed: 676,
passToAssist: 0,
rating: 6.73,
redCards: 1,
saves: 0,
shotsOnTarget: 10,
successfulDribbles: 7,
tackles: 5,
totalShots: 23,
yellowCards: 3,
totalRating: 94.2,
countRating: 14,
totalLongBalls: 1,
totalCross: 2,
totalPasses: 94,
shotsFromInsideTheBox: 20,
appearances: 14,
type: "overall",
id: 0
},
year: "24/25",
startYear: 2024,
endYear: 2025,
team: {
name: "Milan",
slug: "milan",
shortName: "Milan",
gender: "M",
sport: {
name: "Football",
slug: "football",
id: 1
},
userCount: 1718910,
nameCode: "MIL",
disabled: false,
national: false,
type: 0,
id: 2692,
teamColors: {
primary: "#000000",
secondary: "#cc0000",
text: "#cc0000"
},
fieldTranslations: {
nameTranslation: {
ar: "ميلان",
ru: "Милан",
hi: "मिलान",
bn: "মিলান"
},
shortNameTranslation: { }
}
},
uniqueTournament: {
name: "Serie A",
slug: "serie-a",
primaryColorHex: "#09519e",
secondaryColorHex: "#008fd7",
category: {
name: "Italy",
slug: "italy",
sport: {
name: "Football",
slug: "football",
id: 1
},
id: 31,
flag: "italy",
alpha2: "IT",
fieldTranslations: {
nameTranslation: {
ar: "إيطاليا",
hi: "इटली",
bn: "ইতালি"
},
shortNameTranslation: { }
}
},
userCount: 658415,
id: 23,
displayInverseHomeAwayTeams: false,
fieldTranslations: {
nameTranslation: {
ar: "الدوري الإيطالي",
hi: "सीरी ए",
bn: "সিরি আ"
},
shortNameTranslation: { }
},
competitionType: "domestic-league"
},
season: {
name: "Serie A 24/25",
year: "24/25",
editor: false,
id: 63515
}
},
{
statistics: {
accuratePasses: 11,
accuratePassesPercentage: 84.62,
assists: 1,
bigChancesCreated: 1,
bigChancesMissed: 0,
blockedShots: 0,
cleanSheet: 0,
dribbledPast: 1,
errorLeadToGoal: 0,
goals: 0,
goalsAssistsSum: 1,
goalsConceded: 0,
interceptions: 0,
keyPasses: 1,
minutesPlayed: 73,
passToAssist: 0,
rating: 6.6,
redCards: 0,
saves: 0,
shotsOnTarget: 1,
successfulDribbles: 0,
tackles: 1,
totalShots: 1,
yellowCards: 0,
totalRating: 19.8,
countRating: 3,
totalPasses: 13,
shotsFromInsideTheBox: 1,
appearances: 3,
type: "overall",
id: 0
},
year: "24/25",
startYear: 2024,
endYear: 2025,
team: {
name: "Milan",
slug: "milan",
shortName: "Milan",
gender: "M",
sport: {
name: "Football",
slug: "football",
id: 1
},
userCount: 1718910,
nameCode: "MIL",
disabled: false,
national: false,
type: 0,
id: 2692,
teamColors: {
primary: "#000000",
secondary: "#cc0000",
text: "#cc0000"
},
fieldTranslations: {
nameTranslation: {
ar: "ميلان",
ru: "Милан",
hi: "मिलान",
bn: "মিলান"
},
shortNameTranslation: { }
}
},
uniqueTournament: {
name: "Coppa Italia",
slug: "coppa-italia",
primaryColorHex: "#8d041e",
secondaryColorHex: "#bd0a1f",
category: {
name: "Italy",
slug: "italy",
sport: {
name: "Football",
slug: "football",
id: 1
},
id: 31,
flag: "italy",
alpha2: "IT",
fieldTranslations: {
nameTranslation: {
ar: "إيطاليا",
hi: "इटली",
bn: "ইতালি"
},
shortNameTranslation: { }
}
},
userCount: 101994,
id: 328,
displayInverseHomeAwayTeams: false,
fieldTranslations: {
nameTranslation: {
ar: "كأس إيطاليا",
hi: "कोपा इटालिया",
bn: "কোপা ইতালিয়া"
},
shortNameTranslation: { }
},
competitionType: "domestic-cup"
},
season: {
name: "Coppa Italia 24/25",
year: "24/25",
editor: false,
id: 63668
}
},
{
statistics: {
accuratePasses: 9,
accuratePassesPercentage: 64.29,
aerialDuelsWon: 6,
assists: 0,
bigChancesCreated: 0,
bigChancesMissed: 0,
blockedShots: 0,
cleanSheet: 0,
dribbledPast: 2,
errorLeadToGoal: 0,
goals: 0,
goalsAssistsSum: 0,
goalsConceded: 1,
interceptions: 0,
keyPasses: 2,
minutesPlayed: 169,
passToAssist: 0,
rating: 7,
redCards: 0,
saves: 0,
shotsOnTarget: 2,
successfulDribbles: 0,
tackles: 1,
totalShots: 4,
yellowCards: 0,
totalRating: 14,
countRating: 2,
totalPasses: 14,
shotsFromInsideTheBox: 3,
appearances: 2,
type: "overall",
id: 0
},
year: "24/25",
startYear: 2024,
endYear: 2025,
team: {
name: "Mexico",
slug: "mexico",
shortName: "Mexico",
gender: "M",
sport: {
name: "Football",
slug: "football",
id: 1
},
userCount: 262741,
nameCode: "MEX",
ranking: 13,
disabled: false,
national: true,
type: 0,
id: 4781,
teamColors: {
primary: "#1a4d3e",
secondary: "#960000",
text: "#960000"
},
fieldTranslations: {
nameTranslation: {
ar: "المكسيك",
ru: "Мексика",
hi: "मेक्सिको",
bn: "মেক্সিকো"
},
shortNameTranslation: { }
}
},
uniqueTournament: {
name: "CONCACAF Nations League",
slug: "concacaf-nations-league",
primaryColorHex: "#0084cb",
secondaryColorHex: "#d34346",
category: {
name: "North & Central America",
slug: "north-central-america",
sport: {
name: "Football",
slug: "football",
id: 1
},
id: 1469,
flag: "north-and-central-america"
},
userCount: 19938,
id: 14100,
displayInverseHomeAwayTeams: false,
fieldTranslations: {
nameTranslation: {
ar: "دوري أمم الكونكاكاف",
hi: "कोनकाकैफ़ नेशंस लीग",
bn: "কনকাকাফ নেশনস লীগ"
},
shortNameTranslation: { }
},
competitionType: "national"
},
season: {
name: "CONCACAF Nations League 24/25",
year: "24/25",
editor: false,
id: 61662
}
},
{
statistics: {
accuratePasses: 19,
accuratePassesPercentage: 86.36,
aerialDuelsWon: 4,
assists: 0,
bigChancesCreated: 0,
bigChancesMissed: 0,
blockedShots: 0,
cleanSheet: 0,
dribbledPast: 0,
errorLeadToGoal: 0,
expectedAssists: 0.2577697,
expectedGoals: 0.7499,
goals: 1,
goalsAssistsSum: 1,
goalsConceded: 1,
interceptions: 0,
keyPasses: 3,
minutesPlayed: 154,
passToAssist: 0,
rating: 6.95,
redCards: 0,
saves: 0,
shotsOnTarget: 1,
successfulDribbles: 0,
tackles: 0,
totalShots: 3,
yellowCards: 0,
totalRating: 13.9,
countRating: 2,
totalPasses: 22,
shotsFromInsideTheBox: 3,
appearances: 2,
type: "overall",
id: 0
},
year: "24/25",
startYear: 2024,
endYear: 2025,
team: {
name: "Milan",
slug: "milan",
shortName: "Milan",
gender: "M",
sport: {
name: "Football",
slug: "football",
id: 1
},
userCount: 1718910,
nameCode: "MIL",
disabled: false,
national: false,
type: 0,
id: 2692,
teamColors: {
primary: "#000000",
secondary: "#cc0000",
text: "#cc0000"
},
fieldTranslations: {
nameTranslation: {
ar: "ميلان",
ru: "Милан",
hi: "मिलान",
bn: "মিলান"
},
shortNameTranslation: { }
}
},
uniqueTournament: {
name: "UEFA Champions League",
slug: "uefa-champions-league",
primaryColorHex: "#062b5c",
secondaryColorHex: "#086aab",
category: {
name: "Europe",
slug: "europe",
sport: {
name: "Football",
slug: "football",
id: 1
},
id: 1465,
flag: "europe",
fieldTranslations: {
nameTranslation: {
ar: "أوروبا",
hi: "यूरोप",
bn: "ইউরোপ"
},
shortNameTranslation: { }
}
},
userCount: 1095685,
id: 7,
displayInverseHomeAwayTeams: false,
fieldTranslations: {
nameTranslation: {
ar: "دوري أبطال أوروبا",
hi: "यूईएफए चैंपियंस लीग",
bn: "উয়েফা চ্যাম্পিয়ন্স লীগ"
},
shortNameTranslation: { }
},
competitionType: "international-cup"
},
season: {
name: "UEFA Champions League 24/25",
year: "24/25",
editor: false,
seasonCoverageInfo: { },
id: 61644
}
},
{
statistics: {
accurateLongBalls: 2,
accurateLongBallsPercentage: 50,
accuratePasses: 26,
accuratePassesPercentage: 66.67,
aerialDuelsWon: 6,
assists: 1,
bigChancesCreated: 0,
bigChancesMissed: 0,
blockedShots: 1,
outfielderBlocks: 1,
cleanSheet: 1,
dribbledPast: 0,
errorLeadToGoal: 0,
expectedAssists: 0.12206413,
expectedGoals: 2.9161,
goals: 5,
goalsAssistsSum: 6,
goalsConceded: 6,
interceptions: 1,
keyPasses: 3,
minutesPlayed: 295,
passToAssist: 0,
rating: 7.42,
redCards: 0,
saves: 0,
shotsOnTarget: 7,
successfulDribbles: 3,
tackles: 1,
totalShots: 8,
yellowCards: 1,
totalRating: 37.1,
countRating: 5,
totalLongBalls: 4,
totalPasses: 39,
shotsFromInsideTheBox: 8,
appearances: 5,
type: "overall",
id: 0
},
year: "24/25",
startYear: 2024,
endYear: 2025,
team: {
name: "Feyenoord",
slug: "feyenoord",
shortName: "Feyenoord",
gender: "M",
sport: {
name: "Football",
slug: "football",
id: 1
},
userCount: 456983,
nameCode: "FEY",
disabled: false,
national: false,
type: 0,
id: 2959,
teamColors: {
primary: "#ff0000",
secondary: "#ffffff",
text: "#ffffff"
},
fieldTranslations: {
nameTranslation: {
ar: "فينورد",
ru: "Фейеноорд Роттердам",
hi: "फ़ेनोर्ड",
bn: "ফেইনুর্ড"
},
shortNameTranslation: { }
}
},
uniqueTournament: {
name: "UEFA Champions League",
slug: "uefa-champions-league",
primaryColorHex: "#062b5c",
secondaryColorHex: "#086aab",
category: {
name: "Europe",
slug: "europe",
sport: {
name: "Football",
slug: "football",
id: 1
},
id: 1465,
flag: "europe",
fieldTranslations: {
nameTranslation: {
ar: "أوروبا",
hi: "यूरोप",
bn: "ইউরোপ"
},
shortNameTranslation: { }
}
},
userCount: 1095685,
id: 7,
displayInverseHomeAwayTeams: false,
fieldTranslations: {
nameTranslation: {
ar: "دوري أبطال أوروبا",
hi: "यूईएफए चैंपियंस लीग",
bn: "উয়েফা চ্যাম্পিয়ন্স লীগ"
},
shortNameTranslation: { }
},
competitionType: "international-cup"
},
season: {
name: "UEFA Champions League 24/25",
year: "24/25",
editor: false,
seasonCoverageInfo: { },
id: 61644
}
},
{
statistics: {
accurateCrosses: 0,
accurateCrossesPercentage: 0,
accurateLongBalls: 2,
accurateLongBallsPercentage: 50,
accuratePasses: 65,
accuratePassesPercentage: 66.33,
aerialDuelsWon: 12,
assists: 1,
bigChancesCreated: 4,
bigChancesMissed: 7,
blockedShots: 0,
cleanSheet: 0,
dribbledPast: 1,
errorLeadToGoal: 0,
expectedAssists: 0.83971901,
expectedGoals: 7.2632,
goals: 7,
goalsAssistsSum: 8,
goalsConceded: 10,
interceptions: 0,
keyPasses: 11,
minutesPlayed: 770,
passToAssist: 0,
rating: 7.22,
redCards: 0,
saves: 0,
shotsOnTarget: 15,
successfulDribbles: 8,
tackles: 5,
totalShots: 28,
yellowCards: 1,
totalRating: 79.4,
countRating: 11,
totalLongBalls: 4,
totalCross: 2,
totalPasses: 98,
shotsFromInsideTheBox: 26,
appearances: 11,
type: "overall",
id: 0
},
year: "24/25",
startYear: 2024,
endYear: 2025,
team: {
name: "Feyenoord",
slug: "feyenoord",
shortName: "Feyenoord",
gender: "M",
sport: {
name: "Football",
slug: "football",
id: 1
},
userCount: 456983,
nameCode: "FEY",
disabled: false,
national: false,
type: 0,
id: 2959,
teamColors: {
primary: "#ff0000",
secondary: "#ffffff",
text: "#ffffff"
},
fieldTranslations: {
nameTranslation: {
ar: "فينورد",
ru: "Фейеноорд Роттердам",
hi: "फ़ेनोर्ड",
bn: "ফেইনুর্ড"
},
shortNameTranslation: { }
}
},
uniqueTournament: {
name: "VriendenLoterij Eredivisie",
slug: "eredivisie",
primaryColorHex: "#292766",
secondaryColorHex: "#7c79c3",
category: {
name: "Netherlands",
slug: "netherlands",
sport: {
name: "Football",
slug: "football",
id: 1
},
id: 35,
flag: "netherlands",
alpha2: "NL"
},
userCount: 163316,
id: 37,
displayInverseHomeAwayTeams: false,
fieldTranslations: {
nameTranslation: {
ar: "الدوري الهولندي الممتاز",
hi: "इरेडीवीसी",
bn: "এরেডিভিসি"
},
shortNameTranslation: { }
},
competitionType: "domestic-league"
},
season: {
name: "Eredivisie 24/25",
year: "24/25",
editor: false,
id: 61666
}
},
{
statistics: {
accurateLongBalls: 1,
accurateLongBallsPercentage: 50,
accuratePasses: 4,
accuratePassesPercentage: 50,
aerialDuelsWon: 2,
assists: 0,
bigChancesCreated: 0,
bigChancesMissed: 1,
blockedShots: 0,
cleanSheet: 0,
dribbledPast: 0,
errorLeadToGoal: 0,
goals: 2,
goalsAssistsSum: 2,
goalsConceded: 1,
interceptions: 0,
keyPasses: 0,
minutesPlayed: 80,
passToAssist: 0,
rating: 7.3,
redCards: 0,
saves: 0,
shotsOnTarget: 2,
successfulDribbles: 0,
tackles: 0,
totalShots: 4,
yellowCards: 0,
totalRating: 14.6,
countRating: 2,
totalLongBalls: 2,
totalPasses: 8,
shotsFromInsideTheBox: 3,
appearances: 2,
type: "overall",
id: 0
},
year: "24/25",
startYear: 2024,
endYear: 2025,
team: {
name: "Feyenoord",
slug: "feyenoord",
shortName: "Feyenoord",
gender: "M",
sport: {
name: "Football",
slug: "football",
id: 1
},
userCount: 456983,
nameCode: "FEY",
disabled: false,
national: false,
type: 0,
id: 2959,
teamColors: {
primary: "#ff0000",
secondary: "#ffffff",
text: "#ffffff"
},
fieldTranslations: {
nameTranslation: {
ar: "فينورد",
ru: "Фейеноорд Роттердам",
hi: "फ़ेनोर्ड",
bn: "ফেইনুর্ড"
},
shortNameTranslation: { }
}
},
uniqueTournament: {
name: "KNVB Beker",
slug: "knvb-beker",
primaryColorHex: "#3277ad",
category: {
name: "Netherlands",
slug: "netherlands",
sport: {
name: "Football",
slug: "football",
id: 1
},
id: 35,
flag: "netherlands",
alpha2: "NL"
},
userCount: 16661,
id: 330,
displayInverseHomeAwayTeams: false,
fieldTranslations: {
nameTranslation: {
ar: "كأس هولندا",
hi: "केएनवीबी बेकर",
bn: "কেএনভিবি বেকার"
},
shortNameTranslation: { }
},
competitionType: "domestic-cup"
},
season: {
name: "KNVB beker 24/25",
year: "24/25",
editor: false,
id: 67562
}
},
{
statistics: {
accurateCrosses: 1,
accurateCrossesPercentage: 100,
accurateLongBalls: 1,
accurateLongBallsPercentage: 50,
accuratePasses: 21,
accuratePassesPercentage: 63.64,
aerialDuelsWon: 2,
assists: 0,
bigChancesCreated: 0,
bigChancesMissed: 1,
blockedShots: 0,
cleanSheet: 0,
dribbledPast: 0,
errorLeadToGoal: 0,
goals: 0,
goalsAssistsSum: 0,
goalsConceded: 2,
interceptions: 0,
keyPasses: 2,
minutesPlayed: 222,
passToAssist: 0,
rating: 6.63,
redCards: 0,
saves: 0,
shotsOnTarget: 3,
successfulDribbles: 3,
tackles: 0,
totalShots: 6,
yellowCards: 0,
totalRating: 19.9,
countRating: 3,
totalLongBalls: 2,
totalCross: 1,
totalPasses: 33,
shotsFromInsideTheBox: 4,
appearances: 4,
type: "overall",
id: 0
},
year: "2024",
startYear: 2024,
endYear: 2024,
team: {
name: "Mexico",
slug: "mexico",
shortName: "Mexico",
gender: "M",
sport: {
name: "Football",
slug: "football",
id: 1
},
userCount: 262741,
nameCode: "MEX",
ranking: 13,
disabled: false,
national: true,
type: 0,
id: 4781,
teamColors: {
primary: "#1a4d3e",
secondary: "#960000",
text: "#960000"
},
fieldTranslations: {
nameTranslation: {
ar: "المكسيك",
ru: "Мексика",
hi: "मेक्सिको",
bn: "মেক্সিকো"
},
shortNameTranslation: { }
}
},
uniqueTournament: {
name: "International Friendly Games",
slug: "int-friendly-games",
primaryColorHex: "#25497d",
secondaryColorHex: "#d38f1d",
category: {
name: "World",
slug: "world",
sport: {
name: "Football",
slug: "football",
id: 1
},
id: 1468,
flag: "international",
fieldTranslations: {
nameTranslation: {
ar: "العالم",
hi: "विश्व",
bn: "বিশ্ব"
},
shortNameTranslation: { }
}
},
userCount: 75389,
id: 851,
displayInverseHomeAwayTeams: false,
fieldTranslations: {
nameTranslation: {
ar: "مباريات ودية دولية",
hi: "इंटरनेशनल फ्रेंडली गेम्स",
bn: "ইন্টারন্যাশনাল ফ্রেন্ডলি গেমস"
},
shortNameTranslation: { }
},
competitionType: "national"
},
season: {
name: "Int. Friendly Games 2024",
year: "2024",
editor: false,
id: 57198
}
},
{
statistics: {
accurateCrosses: 1,
accurateCrossesPercentage: 100,
accuratePasses: 5,
accuratePassesPercentage: 55.56,
assists: 1,
bigChancesCreated: 2,
bigChancesMissed: 0,
blockedShots: 0,
cleanSheet: 0,
dribbledPast: 0,
errorLeadToGoal: 0,
goals: 2,
goalsAssistsSum: 3,
goalsConceded: 3,
interceptions: 0,
keyPasses: 2,
minutesPlayed: 69,
passToAssist: 0,
rating: 9,
redCards: 0,
saves: 0,
shotsOnTarget: 2,
successfulDribbles: 2,
tackles: 0,
totalShots: 2,
yellowCards: 1,
totalRating: 9,
countRating: 1,
totalCross: 1,
totalPasses: 9,
shotsFromInsideTheBox: 2,
appearances: 1,
type: "overall",
id: 0
},
year: "24/25",
startYear: 2024,
endYear: 2025,
team: {
name: "Feyenoord",
slug: "feyenoord",
shortName: "Feyenoord",
gender: "M",
sport: {
name: "Football",
slug: "football",
id: 1
},
userCount: 456983,
nameCode: "FEY",
disabled: false,
national: false,
type: 0,
id: 2959,
teamColors: {
primary: "#ff0000",
secondary: "#ffffff",
text: "#ffffff"
},
fieldTranslations: {
nameTranslation: {
ar: "فينورد",
ru: "Фейеноорд Роттердам",
hi: "फ़ेनोर्ड",
bn: "ফেইনুর্ড"
},
shortNameTranslation: { }
}
},
uniqueTournament: {
name: "Johan Cruijff Schaal",
slug: "johan-cruijff-schaal",
primaryColorHex: "#f8b331",
secondaryColorHex: "#4343aa",
category: {
name: "Netherlands",
slug: "netherlands",
sport: {
name: "Football",
slug: "football",
id: 1
},
id: 35,
flag: "netherlands",
alpha2: "NL"
},
userCount: 5477,
id: 340,
displayInverseHomeAwayTeams: false,
fieldTranslations: {
nameTranslation: {
ar: "درع يوهان كرويف",
hi: "जोहान क्रुइज्फ़ शाल",
bn: "জোহান ক্রুইজফ স্কাল"
},
shortNameTranslation: { }
},
competitionType: "domestic-cup"
},
season: {
name: "Johan Cruijff Schaal 2024",
year: "24/25",
editor: false,
id: 61052
}
},
{
statistics: {
accurateLongBalls: 1,
accurateLongBallsPercentage: 100,
accuratePasses: 21,
accuratePassesPercentage: 65.63,
aerialDuelsWon: 9,
assists: 0,
bigChancesCreated: 0,
bigChancesMissed: 4,
blockedShots: 0,
cleanSheet: 1,
dribbledPast: 0,
errorLeadToGoal: 0,
expectedAssists: 0.08008351,
expectedGoals: 1.3257,
goals: 0,
goalsAssistsSum: 0,
goalsConceded: 1,
interceptions: 0,
keyPasses: 3,
minutesPlayed: 219,
passToAssist: 0,
rating: 6.37,
redCards: 0,
saves: 0,
shotsOnTarget: 3,
successfulDribbles: 1,
tackles: 3,
totalShots: 8,
yellowCards: 1,
totalRating: 19.1,
countRating: 3,
totalLongBalls: 1,
totalPasses: 32,
shotsFromInsideTheBox: 8,
appearances: 3,
type: "overall",
id: 0
},
year: "2024",
startYear: 2024,
endYear: 2024,
team: {
name: "Mexico",
slug: "mexico",
shortName: "Mexico",
gender: "M",
sport: {
name: "Football",
slug: "football",
id: 1
},
userCount: 262741,
nameCode: "MEX",
ranking: 13,
disabled: false,
national: true,
type: 0,
id: 4781,
teamColors: {
primary: "#1a4d3e",
secondary: "#960000",
text: "#960000"
},
fieldTranslations: {
nameTranslation: {
ar: "المكسيك",
ru: "Мексика",
hi: "मेक्सिको",
bn: "মেক্সিকো"
},
shortNameTranslation: { }
}
},
uniqueTournament: {
name: "Copa América",
slug: "copa-america",
primaryColorHex: "#0A2357",
secondaryColorHex: "#F70F17",
category: {
name: "South America",
slug: "south-america",
sport: {
name: "Football",
slug: "football",
id: 1
},
id: 1470,
flag: "south-america"
},
userCount: 427494,
id: 133,
displayInverseHomeAwayTeams: false,
fieldTranslations: {
nameTranslation: {
ar: "كوبا أمريكا",
hi: "कोपा अमेरिका",
bn: "কোপা আমেরিকা"
},
shortNameTranslation: { }
},
competitionType: "national"
},
season: {
name: "Copa America 2024",
year: "2024",
editor: false,
id: 57114
}
},
{
statistics: {
accurateCrosses: 1,
accurateCrossesPercentage: 16.67,
accurateLongBalls: 7,
accurateLongBallsPercentage: 63.64,
accuratePasses: 265,
accuratePassesPercentage: 69.19,
aerialDuelsWon: 38,
assists: 6,
bigChancesCreated: 9,
bigChancesMissed: 24,
blockedShots: 2,
outfielderBlocks: 2,
cleanSheet: 5,
dribbledPast: 7,
errorLeadToGoal: 0,
expectedAssists: 4.22436812,
expectedGoals: 23.0145,
goals: 23,
goalsAssistsSum: 29,
goalsConceded: 22,
interceptions: 0,
keyPasses: 29,
minutesPlayed: 2384,
passToAssist: 0,
rating: 7.33,
redCards: 0,
saves: 0,
shotsOnTarget: 53,
successfulDribbles: 28,
tackles: 8,
totalShots: 109,
yellowCards: 3,
totalRating: 219.8,
countRating: 30,
totalLongBalls: 11,
totalCross: 6,
totalPasses: 383,
shotsFromInsideTheBox: 96,
appearances: 30,
type: "overall",
id: 0
},
year: "23/24",
startYear: 2023,
endYear: 2024,
team: {
name: "Feyenoord",
slug: "feyenoord",
shortName: "Feyenoord",
gender: "M",
sport: {
name: "Football",
slug: "football",
id: 1
},
userCount: 456983,
nameCode: "FEY",
disabled: false,
national: false,
type: 0,
id: 2959,
teamColors: {
primary: "#ff0000",
secondary: "#ffffff",
text: "#ffffff"
},
fieldTranslations: {
nameTranslation: {
ar: "فينورد",
ru: "Фейеноорд Роттердам",
hi: "फ़ेनोर्ड",
bn: "ফেইনুর্ড"
},
shortNameTranslation: { }
}
},
uniqueTournament: {
name: "VriendenLoterij Eredivisie",
slug: "eredivisie",
primaryColorHex: "#292766",
secondaryColorHex: "#7c79c3",
category: {
name: "Netherlands",
slug: "netherlands",
sport: {
name: "Football",
slug: "football",
id: 1
},
id: 35,
flag: "netherlands",
alpha2: "NL"
},
userCount: 163316,
id: 37,
displayInverseHomeAwayTeams: false,
fieldTranslations: {
nameTranslation: {
ar: "الدوري الهولندي الممتاز",
hi: "इरेडीवीसी",
bn: "এরেডিভিসি"
},
shortNameTranslation: { }
},
competitionType: "domestic-league"
},
season: {
name: "Eredivisie 23/24",
year: "23/24",
editor: false,
id: 52554
}
},
{
statistics: {
accurateCrosses: 0,
accurateCrossesPercentage: 0,
accurateLongBalls: 1,
accurateLongBallsPercentage: 50,
accuratePasses: 40,
accuratePassesPercentage: 60.61,
aerialDuelsWon: 6,
assists: 1,
bigChancesCreated: 0,
bigChancesMissed: 2,
blockedShots: 0,
cleanSheet: 1,
dribbledPast: 0,
errorLeadToGoal: 0,
goals: 0,
goalsAssistsSum: 1,
goalsConceded: 1,
interceptions: 0,
keyPasses: 6,
minutesPlayed: 304,
passToAssist: 0,
rating: 6.82,
redCards: 0,
saves: 0,
shotsOnTarget: 5,
successfulDribbles: 3,
tackles: 4,
totalShots: 7,
yellowCards: 2,
totalRating: 27.3,
countRating: 4,
totalLongBalls: 2,
totalCross: 1,
totalPasses: 66,
shotsFromInsideTheBox: 7,
appearances: 4,
type: "overall",
id: 0
},
year: "23/24",
startYear: 2023,
endYear: 2024,
team: {
name: "Feyenoord",
slug: "feyenoord",
shortName: "Feyenoord",
gender: "M",
sport: {
name: "Football",
slug: "football",
id: 1
},
userCount: 456983,
nameCode: "FEY",
disabled: false,
national: false,
type: 0,
id: 2959,
teamColors: {
primary: "#ff0000",
secondary: "#ffffff",
text: "#ffffff"
},
fieldTranslations: {
nameTranslation: {
ar: "فينورد",
ru: "Фейеноорд Роттердам",
hi: "फ़ेनोर्ड",
bn: "ফেইনুর্ড"
},
shortNameTranslation: { }
}
},
uniqueTournament: {
name: "KNVB Beker",
slug: "knvb-beker",
primaryColorHex: "#3277ad",
category: {
name: "Netherlands",
slug: "netherlands",
sport: {
name: "Football",
slug: "football",
id: 1
},
id: 35,
flag: "netherlands",
alpha2: "NL"
},
userCount: 16661,
id: 330,
displayInverseHomeAwayTeams: false,
fieldTranslations: {
nameTranslation: {
ar: "كأس هولندا",
hi: "केएनवीबी बेकर",
bn: "কেএনভিবি বেকার"
},
shortNameTranslation: { }
},
competitionType: "domestic-cup"
},
season: {
name: "KNVB beker 23/24",
year: "23/24",
editor: false,
id: 55337
}
},
{
statistics: {
accurateLongBalls: 0,
accurateLongBallsPercentage: 0,
accuratePasses: 16,
accuratePassesPercentage: 61.54,
aerialDuelsWon: 6,
assists: 1,
bigChancesCreated: 0,
bigChancesMissed: 0,
blockedShots: 0,
cleanSheet: 0,
dribbledPast: 0,
errorLeadToGoal: 0,
goals: 0,
goalsAssistsSum: 1,
goalsConceded: 1,
interceptions: 0,
keyPasses: 3,
minutesPlayed: 133,
passToAssist: 0,
rating: 6.87,
redCards: 0,
saves: 0,
shotsOnTarget: 0,
successfulDribbles: 0,
tackles: 1,
totalShots: 5,
yellowCards: 1,
totalRating: 20.6,
countRating: 3,
totalLongBalls: 2,
totalPasses: 26,
shotsFromInsideTheBox: 5,
appearances: 3,
type: "overall",
id: 0
},
year: "23/24",
startYear: 2023,
endYear: 2024,
team: {
name: "Mexico",
slug: "mexico",
shortName: "Mexico",
gender: "M",
sport: {
name: "Football",
slug: "football",
id: 1
},
userCount: 262741,
nameCode: "MEX",
ranking: 13,
disabled: false,
national: true,
type: 0,
id: 4781,
teamColors: {
primary: "#1a4d3e",
secondary: "#960000",
text: "#960000"
},
fieldTranslations: {
nameTranslation: {
ar: "المكسيك",
ru: "Мексика",
hi: "मेक्सिको",
bn: "মেক্সিকো"
},
shortNameTranslation: { }
}
},
uniqueTournament: {
name: "CONCACAF Nations League",
slug: "concacaf-nations-league",
primaryColorHex: "#0084cb",
secondaryColorHex: "#d34346",
category: {
name: "North & Central America",
slug: "north-central-america",
sport: {
name: "Football",
slug: "football",
id: 1
},
id: 1469,
flag: "north-and-central-america"
},
userCount: 19938,
id: 14100,
displayInverseHomeAwayTeams: false,
fieldTranslations: {
nameTranslation: {
ar: "دوري أمم الكونكاكاف",
hi: "कोनकाकैफ़ नेशंस लीग",
bn: "কনকাকাফ নেশনস লীগ"
},
shortNameTranslation: { }
},
competitionType: "national"
},
season: {
name: "CONCACAF Nations League 23/24",
year: "23/24",
editor: false,
id: 53046
}
},
{
statistics: {
accurateLongBalls: 1,
accurateLongBallsPercentage: 50,
accuratePasses: 10,
accuratePassesPercentage: 66.67,
aerialDuelsWon: 1,
assists: 0,
bigChancesCreated: 1,
bigChancesMissed: 0,
blockedShots: 0,
cleanSheet: 0,
dribbledPast: 0,
errorLeadToGoal: 0,
expectedAssists: 0.02642593,
expectedGoals: 0.4049,
goals: 1,
goalsAssistsSum: 1,
goalsConceded: 2,
interceptions: 0,
keyPasses: 1,
minutesPlayed: 105,
passToAssist: 0,
rating: 7.2,
redCards: 0,
saves: 0,
shotsOnTarget: 2,
successfulDribbles: 0,
tackles: 1,
totalShots: 5,
yellowCards: 0,
totalRating: 14.4,
countRating: 2,
totalLongBalls: 2,
totalPasses: 15,
shotsFromInsideTheBox: 5,
appearances: 2,
type: "overall",
id: 0
},
year: "23/24",
startYear: 2023,
endYear: 2024,
team: {
name: "Feyenoord",
slug: "feyenoord",
shortName: "Feyenoord",
gender: "M",
sport: {
name: "Football",
slug: "football",
id: 1
},
userCount: 456983,
nameCode: "FEY",
disabled: false,
national: false,
type: 0,
id: 2959,
teamColors: {
primary: "#ff0000",
secondary: "#ffffff",
text: "#ffffff"
},
fieldTranslations: {
nameTranslation: {
ar: "فينورد",
ru: "Фейеноорд Роттердам",
hi: "फ़ेनोर्ड",
bn: "ফেইনুর্ড"
},
shortNameTranslation: { }
}
},
uniqueTournament: {
name: "UEFA Europa League",
slug: "uefa-europa-league",
secondaryColorHex: "#f37d25",
category: {
name: "Europe",
slug: "europe",
sport: {
name: "Football",
slug: "football",
id: 1
},
id: 1465,
flag: "europe",
fieldTranslations: {
nameTranslation: {
ar: "أوروبا",
hi: "यूरोप",
bn: "ইউরোপ"
},
shortNameTranslation: { }
}
},
userCount: 493467,
id: 679,
displayInverseHomeAwayTeams: false,
fieldTranslations: {
nameTranslation: {
ar: "الدوري الأوروبي",
hi: "यूईएफए यूरोपा लीग",
bn: "উয়েফা ইউরোপা লীগ"
},
shortNameTranslation: { }
},
competitionType: "international-cup"
},
season: {
name: "UEFA Europa League 23/24",
year: "23/24",
editor: false,
id: 53654
}
},
{
statistics: {
accurateCrosses: 0,
accurateCrossesPercentage: 0,
accurateLongBalls: 0,
accurateLongBallsPercentage: 0,
accuratePasses: 33,
accuratePassesPercentage: 70.21,
aerialDuelsWon: 3,
assists: 1,
bigChancesCreated: 1,
bigChancesMissed: 4,
blockedShots: 0,
cleanSheet: 0,
dribbledPast: 2,
errorLeadToGoal: 0,
expectedAssists: 0.31034423,
expectedGoals: 2.2915,
goals: 2,
goalsAssistsSum: 3,
goalsConceded: 6,
interceptions: 1,
keyPasses: 2,
minutesPlayed: 349,
passToAssist: 0,
rating: 6.88,
redCards: 0,
saves: 0,
shotsOnTarget: 6,
successfulDribbles: 4,
tackles: 0,
totalShots: 11,
yellowCards: 1,
totalRating: 27.5,
countRating: 4,
totalLongBalls: 1,
totalCross: 1,
totalPasses: 47,
shotsFromInsideTheBox: 7,
appearances: 4,
type: "overall",
id: 0
},
year: "23/24",
startYear: 2023,
endYear: 2024,
team: {
name: "Feyenoord",
slug: "feyenoord",
shortName: "Feyenoord",
gender: "M",
sport: {
name: "Football",
slug: "football",
id: 1
},
userCount: 456983,
nameCode: "FEY",
disabled: false,
national: false,
type: 0,
id: 2959,
teamColors: {
primary: "#ff0000",
secondary: "#ffffff",
text: "#ffffff"
},
fieldTranslations: {
nameTranslation: {
ar: "فينورد",
ru: "Фейеноорд Роттердам",
hi: "फ़ेनोर्ड",
bn: "ফেইনুর্ড"
},
shortNameTranslation: { }
}
},
uniqueTournament: {
name: "UEFA Champions League",
slug: "uefa-champions-league",
primaryColorHex: "#062b5c",
secondaryColorHex: "#086aab",
category: {
name: "Europe",
slug: "europe",
sport: {
name: "Football",
slug: "football",
id: 1
},
id: 1465,
flag: "europe",
fieldTranslations: {
nameTranslation: {
ar: "أوروبا",
hi: "यूरोप",
bn: "ইউরোপ"
},
shortNameTranslation: { }
}
},
userCount: 1095685,
id: 7,
displayInverseHomeAwayTeams: false,
fieldTranslations: {
nameTranslation: {
ar: "دوري أبطال أوروبا",
hi: "यूईएफए चैंपियंस लीग",
bn: "উয়েফা চ্যাম্পিয়ন্স লীগ"
},
shortNameTranslation: { }
},
competitionType: "international-cup"
},
season: {
name: "UEFA Champions League 23/24",
year: "23/24",
editor: false,
seasonCoverageInfo: { },
id: 52162
}
},
{
statistics: {
accurateLongBalls: 1,
accurateLongBallsPercentage: 100,
accuratePasses: 17,
accuratePassesPercentage: 65.38,
aerialDuelsWon: 4,
assists: 0,
bigChancesCreated: 0,
bigChancesMissed: 2,
blockedShots: 0,
cleanSheet: 0,
dribbledPast: 1,
errorLeadToGoal: 0,
goals: 0,
goalsAssistsSum: 0,
goalsConceded: 4,
interceptions: 0,
keyPasses: 0,
minutesPlayed: 167,
passToAssist: 0,
rating: 6.45,
redCards: 0,
saves: 0,
shotsOnTarget: 1,
successfulDribbles: 2,
tackles: 1,
totalShots: 5,
yellowCards: 0,
totalRating: 25.8,
countRating: 4,
totalLongBalls: 1,
totalPasses: 26,
shotsFromInsideTheBox: 5,
appearances: 4,
type: "overall",
id: 0
},
year: "2023",
startYear: 2023,
endYear: 2023,
team: {
name: "Mexico",
slug: "mexico",
shortName: "Mexico",
gender: "M",
sport: {
name: "Football",
slug: "football",
id: 1
},
userCount: 262741,
nameCode: "MEX",
ranking: 13,
disabled: false,
national: true,
type: 0,
id: 4781,
teamColors: {
primary: "#1a4d3e",
secondary: "#960000",
text: "#960000"
},
fieldTranslations: {
nameTranslation: {
ar: "المكسيك",
ru: "Мексика",
hi: "मेक्सिको",
bn: "মেক্সিকো"
},
shortNameTranslation: { }
}
},
uniqueTournament: {
name: "International Friendly Games",
slug: "int-friendly-games",
primaryColorHex: "#25497d",
secondaryColorHex: "#d38f1d",
category: {
name: "World",
slug: "world",
sport: {
name: "Football",
slug: "football",
id: 1
},
id: 1468,
flag: "international",
fieldTranslations: {
nameTranslation: {
ar: "العالم",
hi: "विश्व",
bn: "বিশ্ব"
},
shortNameTranslation: { }
}
},
userCount: 75389,
id: 851,
displayInverseHomeAwayTeams: false,
fieldTranslations: {
nameTranslation: {
ar: "مباريات ودية دولية",
hi: "इंटरनेशनल फ्रेंडली गेम्स",
bn: "ইন্টারন্যাশনাল ফ্রেন্ডলি গেমস"
},
shortNameTranslation: { }
},
competitionType: "national"
},
season: {
name: "Int. Friendly Games 2023",
year: "2023",
editor: false,
id: 47776
}
},
{
statistics: {
accuratePasses: 7,
accuratePassesPercentage: 87.5,
aerialDuelsWon: 1,
assists: 0,
bigChancesCreated: 0,
bigChancesMissed: 0,
outfielderBlocks: 1,
cleanSheet: 0,
dribbledPast: 0,
errorLeadToGoal: 0,
goals: 0,
goalsAssistsSum: 0,
goalsConceded: 0,
interceptions: 0,
keyPasses: 0,
minutesPlayed: 62,
passToAssist: 0,
rating: 6.9,
redCards: 0,
saves: 0,
successfulDribbles: 2,
tackles: 0,
yellowCards: 0,
totalRating: 6.9,
countRating: 1,
totalPasses: 8,
shotsFromInsideTheBox: 0,
appearances: 1,
type: "overall",
id: 0
},
year: "23/24",
startYear: 2023,
endYear: 2024,
team: {
name: "Feyenoord",
slug: "feyenoord",
shortName: "Feyenoord",
gender: "M",
sport: {
name: "Football",
slug: "football",
id: 1
},
userCount: 456983,
nameCode: "FEY",
disabled: false,
national: false,
type: 0,
id: 2959,
teamColors: {
primary: "#ff0000",
secondary: "#ffffff",
text: "#ffffff"
},
fieldTranslations: {
nameTranslation: {
ar: "فينورد",
ru: "Фейеноорд Роттердам",
hi: "फ़ेनोर्ड",
bn: "ফেইনুর্ড"
},
shortNameTranslation: { }
}
},
uniqueTournament: {
name: "Johan Cruijff Schaal",
slug: "johan-cruijff-schaal",
primaryColorHex: "#f8b331",
secondaryColorHex: "#4343aa",
category: {
name: "Netherlands",
slug: "netherlands",
sport: {
name: "Football",
slug: "football",
id: 1
},
id: 35,
flag: "netherlands",
alpha2: "NL"
},
userCount: 5477,
id: 340,
displayInverseHomeAwayTeams: false,
fieldTranslations: {
nameTranslation: {
ar: "درع يوهان كرويف",
hi: "जोहान क्रुइज्फ़ शाल",
bn: "জোহান ক্রুইজফ স্কাল"
},
shortNameTranslation: { }
},
competitionType: "domestic-cup"
},
season: {
name: "Johan Cruijff Schaal 2023",
year: "23/24",
editor: false,
id: 52044
}
},
{
statistics: {
accuratePasses: 24,
accuratePassesPercentage: 68.57,
aerialDuelsWon: 6,
assists: 0,
bigChancesCreated: 0,
bigChancesMissed: 4,
blockedShots: 0,
cleanSheet: 0,
dribbledPast: 1,
errorLeadToGoal: 0,
goals: 2,
goalsAssistsSum: 2,
goalsConceded: 2,
interceptions: 0,
keyPasses: 0,
minutesPlayed: 208,
passToAssist: 0,
rating: 6.57,
redCards: 0,
saves: 0,
shotsOnTarget: 6,
successfulDribbles: 6,
tackles: 2,
totalShots: 10,
yellowCards: 1,
totalRating: 39.4,
countRating: 6,
totalPasses: 35,
shotsFromInsideTheBox: 9,
appearances: 6,
type: "overall",
id: 0
},
year: "2023",
startYear: 2023,
endYear: 2023,
team: {
name: "Mexico",
slug: "mexico",
shortName: "Mexico",
gender: "M",
sport: {
name: "Football",
slug: "football",
id: 1
},
userCount: 262741,
nameCode: "MEX",
ranking: 13,
disabled: false,
national: true,
type: 0,
id: 4781,
teamColors: {
primary: "#1a4d3e",
secondary: "#960000",
text: "#960000"
},
fieldTranslations: {
nameTranslation: {
ar: "المكسيك",
ru: "Мексика",
hi: "मेक्सिको",
bn: "মেক্সিকো"
},
shortNameTranslation: { }
}
},
uniqueTournament: {
name: "CONCACAF Gold Cup",
slug: "concacaf-gold-cup",
primaryColorHex: "#031236",
secondaryColorHex: "#ffc84e",
category: {
name: "North & Central America",
slug: "north-central-america",
sport: {
name: "Football",
slug: "football",
id: 1
},
id: 1469,
flag: "north-and-central-america"
},
userCount: 46431,
id: 140,
displayInverseHomeAwayTeams: false,
fieldTranslations: {
nameTranslation: {
ar: "كأس الكونكاكاف الذهبي",
hi: "कोंकाकाफ गोल्ड कप",
bn: "কনকাক্যাফ গোল্ড কাপ"
},
shortNameTranslation: { }
},
competitionType: "national"
},
season: {
name: "Gold Cup 2023",
year: "2023",
editor: false,
id: 50492
}
},
{
statistics: {
accurateCrosses: 0,
accurateCrossesPercentage: 0,
accurateLongBalls: 2,
accurateLongBallsPercentage: 66.67,
accuratePasses: 30,
accuratePassesPercentage: 71.43,
aerialDuelsWon: 8,
assists: 0,
bigChancesCreated: 0,
bigChancesMissed: 1,
blockedShots: 0,
cleanSheet: 1,
dribbledPast: 1,
errorLeadToGoal: 0,
goals: 0,
goalsAssistsSum: 0,
goalsConceded: 2,
interceptions: 1,
keyPasses: 1,
minutesPlayed: 316,
passToAssist: 0,
rating: 6.4,
redCards: 0,
saves: 0,
shotsOnTarget: 1,
successfulDribbles: 2,
tackles: 0,
totalShots: 6,
yellowCards: 1,
totalRating: 32,
countRating: 5,
totalLongBalls: 3,
totalCross: 1,
totalPasses: 42,
shotsFromInsideTheBox: 5,
appearances: 5,
type: "overall",
id: 0
},
year: "22/23",
startYear: 2022,
endYear: 2023,
team: {
name: "Mexico",
slug: "mexico",
shortName: "Mexico",
gender: "M",
sport: {
name: "Football",
slug: "football",
id: 1
},
userCount: 262741,
nameCode: "MEX",
ranking: 13,
disabled: false,
national: true,
type: 0,
id: 4781,
teamColors: {
primary: "#1a4d3e",
secondary: "#960000",
text: "#960000"
},
fieldTranslations: {
nameTranslation: {
ar: "المكسيك",
ru: "Мексика",
hi: "मेक्सिको",
bn: "মেক্সিকো"
},
shortNameTranslation: { }
}
},
uniqueTournament: {
name: "CONCACAF Nations League",
slug: "concacaf-nations-league",
primaryColorHex: "#0084cb",
secondaryColorHex: "#d34346",
category: {
name: "North & Central America",
slug: "north-central-america",
sport: {
name: "Football",
slug: "football",
id: 1
},
id: 1469,
flag: "north-and-central-america"
},
userCount: 19938,
id: 14100,
displayInverseHomeAwayTeams: false,
fieldTranslations: {
nameTranslation: {
ar: "دوري أمم الكونكاكاف",
hi: "कोनकाकैफ़ नेशंस लीग",
bn: "কনকাকাফ নেশনস লীগ"
},
shortNameTranslation: { }
},
competitionType: "national"
},
season: {
name: "CONCACAF Nations League 22/23",
year: "22/23",
editor: false,
id: 41713
}
},
{
statistics: {
accurateCrosses: 0,
accurateCrossesPercentage: 0,
accurateLongBalls: 4,
accurateLongBallsPercentage: 44.44,
accuratePasses: 205,
accuratePassesPercentage: 70.21,
aerialDuelsWon: 33,
assists: 2,
bigChancesCreated: 3,
bigChancesMissed: 15,
blockedShots: 0,
cleanSheet: 2,
dribbledPast: 10,
errorLeadToGoal: 0,
goals: 15,
goalsAssistsSum: 17,
goalsConceded: 16,
interceptions: 4,
keyPasses: 20,
minutesPlayed: 1932,
passToAssist: 0,
rating: 6.91,
redCards: 0,
saves: 0,
shotsOnTarget: 30,
successfulDribbles: 14,
tackles: 11,
totalShots: 86,
yellowCards: 3,
totalRating: 221,
countRating: 32,
totalLongBalls: 9,
totalCross: 1,
totalPasses: 292,
shotsFromInsideTheBox: 74,
appearances: 32,
type: "overall",
id: 0
},
year: "22/23",
startYear: 2022,
endYear: 2023,
team: {
name: "Feyenoord",
slug: "feyenoord",
shortName: "Feyenoord",
gender: "M",
sport: {
name: "Football",
slug: "football",
id: 1
},
userCount: 456983,
nameCode: "FEY",
disabled: false,
national: false,
type: 0,
id: 2959,
teamColors: {
primary: "#ff0000",
secondary: "#ffffff",
text: "#ffffff"
},
fieldTranslations: {
nameTranslation: {
ar: "فينورد",
ru: "Фейеноорд Роттердам",
hi: "फ़ेनोर्ड",
bn: "ফেইনুর্ড"
},
shortNameTranslation: { }
}
},
uniqueTournament: {
name: "VriendenLoterij Eredivisie",
slug: "eredivisie",
primaryColorHex: "#292766",
secondaryColorHex: "#7c79c3",
category: {
name: "Netherlands",
slug: "netherlands",
sport: {
name: "Football",
slug: "football",
id: 1
},
id: 35,
flag: "netherlands",
alpha2: "NL"
},
userCount: 163316,
id: 37,
displayInverseHomeAwayTeams: false,
fieldTranslations: {
nameTranslation: {
ar: "الدوري الهولندي الممتاز",
hi: "इरेडीवीसी",
bn: "এরেডিভিসি"
},
shortNameTranslation: { }
},
competitionType: "domestic-league"
},
season: {
name: "Eredivisie 22/23",
year: "22/23",
editor: false,
seasonCoverageInfo: { },
id: 42256
}
},
{
statistics: {
accurateLongBalls: 2,
accurateLongBallsPercentage: 66.67,
accuratePasses: 41,
accuratePassesPercentage: 64.06,
aerialDuelsWon: 10,
assists: 0,
bigChancesCreated: 0,
bigChancesMissed: 0,
blockedShots: 1,
outfielderBlocks: 1,
cleanSheet: 0,
dribbledPast: 2,
errorLeadToGoal: 0,
expectedAssists: 0.22619671,
expectedGoals: 3.0573,
goals: 5,
goalsAssistsSum: 5,
goalsConceded: 8,
interceptions: 1,
keyPasses: 3,
minutesPlayed: 439,
passToAssist: 0,
rating: 7.01,
redCards: 1,
saves: 0,
shotsOnTarget: 5,
successfulDribbles: 6,
tackles: 4,
totalShots: 13,
yellowCards: 2,
totalRating: 63.1,
countRating: 9,
totalLongBalls: 3,
totalPasses: 64,
shotsFromInsideTheBox: 12,
appearances: 9,
type: "overall",
id: 0
},
year: "22/23",
startYear: 2022,
endYear: 2023,
team: {
name: "Feyenoord",
slug: "feyenoord",
shortName: "Feyenoord",
gender: "M",
sport: {
name: "Football",
slug: "football",
id: 1
},
userCount: 456983,
nameCode: "FEY",
disabled: false,
national: false,
type: 0,
id: 2959,
teamColors: {
primary: "#ff0000",
secondary: "#ffffff",
text: "#ffffff"
},
fieldTranslations: {
nameTranslation: {
ar: "فينورد",
ru: "Фейеноорд Роттердам",
hi: "फ़ेनोर्ड",
bn: "ফেইনুর্ড"
},
shortNameTranslation: { }
}
},
uniqueTournament: {
name: "UEFA Europa League",
slug: "uefa-europa-league",
secondaryColorHex: "#f37d25",
category: {
name: "Europe",
slug: "europe",
sport: {
name: "Football",
slug: "football",
id: 1
},
id: 1465,
flag: "europe",
fieldTranslations: {
nameTranslation: {
ar: "أوروبا",
hi: "यूरोप",
bn: "ইউরোপ"
},
shortNameTranslation: { }
}
},
userCount: 493467,
id: 679,
displayInverseHomeAwayTeams: false,
fieldTranslations: {
nameTranslation: {
ar: "الدوري الأوروبي",
hi: "यूईएफए यूरोपा लीग",
bn: "উয়েফা ইউরোপা লীগ"
},
shortNameTranslation: { }
},
competitionType: "international-cup"
},
season: {
name: "UEFA Europa League 22/23",
year: "22/23",
editor: false,
seasonCoverageInfo: { },
id: 44509
}
},
{
statistics: {
accurateLongBalls: 0,
accurateLongBallsPercentage: 0,
accuratePasses: 31,
accuratePassesPercentage: 77.5,
aerialDuelsWon: 6,
assists: 0,
bigChancesCreated: 1,
bigChancesMissed: 1,
blockedShots: 0,
cleanSheet: 0,
dribbledPast: 1,
errorLeadToGoal: 0,
goals: 3,
goalsAssistsSum: 3,
goalsConceded: 4,
interceptions: 0,
keyPasses: 1,
minutesPlayed: 265,
passToAssist: 0,
rating: 7.35,
redCards: 0,
saves: 0,
shotsOnTarget: 9,
successfulDribbles: 3,
tackles: 1,
totalShots: 15,
yellowCards: 0,
totalRating: 29.4,
countRating: 4,
totalLongBalls: 1,
totalPasses: 40,
shotsFromInsideTheBox: 14,
appearances: 4,
type: "overall",
id: 0
},
year: "22/23",
startYear: 2022,
endYear: 2023,
team: {
name: "Feyenoord",
slug: "feyenoord",
shortName: "Feyenoord",
gender: "M",
sport: {
name: "Football",
slug: "football",
id: 1
},
userCount: 456983,
nameCode: "FEY",
disabled: false,
national: false,
type: 0,
id: 2959,
teamColors: {
primary: "#ff0000",
secondary: "#ffffff",
text: "#ffffff"
},
fieldTranslations: {
nameTranslation: {
ar: "فينورد",
ru: "Фейеноорд Роттердам",
hi: "फ़ेनोर्ड",
bn: "ফেইনুর্ড"
},
shortNameTranslation: { }
}
},
uniqueTournament: {
name: "KNVB Beker",
slug: "knvb-beker",
primaryColorHex: "#3277ad",
category: {
name: "Netherlands",
slug: "netherlands",
sport: {
name: "Football",
slug: "football",
id: 1
},
id: 35,
flag: "netherlands",
alpha2: "NL"
},
userCount: 16661,
id: 330,
displayInverseHomeAwayTeams: false,
fieldTranslations: {
nameTranslation: {
ar: "كأس هولندا",
hi: "केएनवीबी बेकर",
bn: "কেএনভিবি বেকার"
},
shortNameTranslation: { }
},
competitionType: "domestic-cup"
},
season: {
name: "KNVB beker 22/23",
year: "22/23",
editor: false,
id: 46333
}
},
{
statistics: {
accuratePasses: 6,
accuratePassesPercentage: 85.71,
aerialDuelsWon: 1,
assists: 0,
bigChancesCreated: 0,
bigChancesMissed: 0,
cleanSheet: 0,
dribbledPast: 1,
errorLeadToGoal: 0,
goals: 0,
goalsAssistsSum: 0,
goalsConceded: 1,
interceptions: 0,
keyPasses: 0,
minutesPlayed: 30,
passToAssist: 0,
rating: 6.5,
redCards: 0,
saves: 0,
successfulDribbles: 0,
tackles: 0,
yellowCards: 0,
totalRating: 6.5,
countRating: 1,
totalPasses: 7,
shotsFromInsideTheBox: 0,
appearances: 1,
type: "overall",
id: 0
},
year: "2022",
startYear: 2022,
endYear: 2022,
team: {
name: "Mexico",
slug: "mexico",
shortName: "Mexico",
gender: "M",
sport: {
name: "Football",
slug: "football",
id: 1
},
userCount: 262741,
nameCode: "MEX",
ranking: 13,
disabled: false,
national: true,
type: 0,
id: 4781,
teamColors: {
primary: "#1a4d3e",
secondary: "#960000",
text: "#960000"
},
fieldTranslations: {
nameTranslation: {
ar: "المكسيك",
ru: "Мексика",
hi: "मेक्सिको",
bn: "মেক্সিকো"
},
shortNameTranslation: { }
}
},
uniqueTournament: {
name: "International Friendly Games",
slug: "int-friendly-games",
primaryColorHex: "#25497d",
secondaryColorHex: "#d38f1d",
category: {
name: "World",
slug: "world",
sport: {
name: "Football",
slug: "football",
id: 1
},
id: 1468,
flag: "international",
fieldTranslations: {
nameTranslation: {
ar: "العالم",
hi: "विश्व",
bn: "বিশ্ব"
},
shortNameTranslation: { }
}
},
userCount: 75389,
id: 851,
displayInverseHomeAwayTeams: false,
fieldTranslations: {
nameTranslation: {
ar: "مباريات ودية دولية",
hi: "इंटरनेशनल फ्रेंडली गेम्स",
bn: "ইন্টারন্যাশনাল ফ্রেন্ডলি গেমস"
},
shortNameTranslation: { }
},
competitionType: "national"
},
season: {
name: "Int. Friendly Games 2022",
year: "2022",
editor: false,
id: 40241
}
},
{
statistics: {
accurateLongBalls: 1,
accurateLongBallsPercentage: 16.67,
accuratePasses: 55,
accuratePassesPercentage: 58.51,
aerialDuelsWon: 19,
assists: 0,
bigChancesCreated: 1,
bigChancesMissed: 1,
blockedShots: 0,
cleanSheet: 0,
dribbledPast: 0,
errorLeadToGoal: 0,
goals: 5,
goalsAssistsSum: 5,
goalsConceded: 9,
interceptions: 0,
keyPasses: 6,
minutesPlayed: 409,
passToAssist: 0,
rating: 7.18,
redCards: 0,
saves: 0,
shotsOnTarget: 7,
successfulDribbles: 5,
tackles: 1,
totalShots: 15,
yellowCards: 0,
totalRating: 35.9,
countRating: 5,
totalLongBalls: 6,
totalPasses: 94,
shotsFromInsideTheBox: 14,
appearances: 5,
type: "overall",
id: 0
},
year: "2022",
startYear: 2022,
endYear: 2022,
team: {
name: "Cruz Azul",
slug: "cruz-azul",
shortName: "Cruz Azul",
gender: "M",
sport: {
name: "Football",
slug: "football",
id: 1
},
userCount: 68602,
nameCode: "CAZ",
disabled: false,
national: false,
type: 0,
id: 1947,
teamColors: {
primary: "#0080c0",
secondary: "#ffffff",
text: "#ffffff"
},
fieldTranslations: {
nameTranslation: {
ar: "كروز أزول",
ru: "Круз Азул"
},
shortNameTranslation: { }
}
},
uniqueTournament: {
name: "Liga MX, Apertura",
slug: "liga-mx-apertura",
primaryColorHex: "#cd2c25",
secondaryColorHex: "#52b030",
category: {
name: "Mexico",
slug: "mexico",
sport: {
name: "Football",
slug: "football",
id: 1
},
id: 12,
flag: "mexico",
alpha2: "MX"
},
userCount: 39667,
id: 11621,
displayInverseHomeAwayTeams: false,
fieldTranslations: {
nameTranslation: {
ar: "دوري المكسيك، مرحلة الذهاب",
hi: "लीगा एमएक्स, एपर्टुरा",
bn: "লিগা এমএক্স, অ্যাপেরতুরা"
},
shortNameTranslation: { }
},
competitionType: "domestic-league"
},
season: {
name: "Primera Division, Apertura 2022",
year: "22/23",
editor: false,
id: 42017
}
},
{
statistics: {
accuratePasses: 9,
accuratePassesPercentage: 50,
aerialDuelsWon: 7,
assists: 0,
bigChancesCreated: 0,
bigChancesMissed: 1,
blockedShots: 1,
outfielderBlocks: 1,
cleanSheet: 0,
dribbledPast: 1,
errorLeadToGoal: 0,
goals: 1,
goalsAssistsSum: 1,
goalsConceded: 2,
interceptions: 0,
keyPasses: 0,
minutesPlayed: 90,
passToAssist: 0,
rating: 7.4,
redCards: 0,
saves: 0,
shotsOnTarget: 2,
successfulDribbles: 2,
tackles: 1,
totalShots: 4,
yellowCards: 1,
totalRating: 7.4,
countRating: 1,
totalPasses: 18,
shotsFromInsideTheBox: 3,
appearances: 1,
type: "overall",
id: 0
},
year: "2022",
startYear: 2022,
endYear: 2022,
team: {
name: "Cruz Azul",
slug: "cruz-azul",
shortName: "Cruz Azul",
gender: "M",
sport: {
name: "Football",
slug: "football",
id: 1
},
userCount: 68602,
nameCode: "CAZ",
disabled: false,
national: false,
type: 0,
id: 1947,
teamColors: {
primary: "#0080c0",
secondary: "#ffffff",
text: "#ffffff"
},
fieldTranslations: {
nameTranslation: {
ar: "كروز أزول",
ru: "Круз Азул"
},
shortNameTranslation: { }
}
},
uniqueTournament: {
name: "Supercopa Liga MX",
slug: "supercopa-liga-mx",
primaryColorHex: "#AA9759",
secondaryColorHex: "#B2AC9D",
category: {
name: "Mexico",
slug: "mexico",
sport: {
name: "Football",
slug: "football",
id: 1
},
id: 12,
flag: "mexico",
alpha2: "MX"
},
userCount: 751,
id: 18872,
displayInverseHomeAwayTeams: false,
competitionType: "domestic-cup"
},
season: {
name: "Supercopa Liga MX 2022",
year: "2022",
editor: false,
id: 42281
}
},
{
statistics: {
accurateCrosses: 0,
accurateCrossesPercentage: 0,
accurateLongBalls: 1,
accurateLongBallsPercentage: 100,
accuratePasses: 90,
accuratePassesPercentage: 62.94,
aerialDuelsWon: 35,
assists: 1,
bigChancesCreated: 2,
bigChancesMissed: 3,
blockedShots: 1,
outfielderBlocks: 1,
cleanSheet: 1,
dribbledPast: 2,
errorLeadToGoal: 0,
goals: 3,
goalsAssistsSum: 4,
goalsConceded: 7,
interceptions: 3,
keyPasses: 7,
minutesPlayed: 714,
passToAssist: 0,
rating: 6.71,
redCards: 1,
saves: 0,
shotsOnTarget: 8,
successfulDribbles: 6,
tackles: 5,
totalShots: 27,
yellowCards: 3,
totalRating: 120.7,
countRating: 18,
totalLongBalls: 1,
totalCross: 1,
totalPasses: 143,
shotsFromInsideTheBox: 24,
appearances: 18,
type: "overall",
id: 0
},
year: "2022",
startYear: 2022,
endYear: 2022,
team: {
name: "Cruz Azul",
slug: "cruz-azul",
shortName: "Cruz Azul",
gender: "M",
sport: {
name: "Football",
slug: "football",
id: 1
},
userCount: 68602,
nameCode: "CAZ",
disabled: false,
national: false,
type: 0,
id: 1947,
teamColors: {
primary: "#0080c0",
secondary: "#ffffff",
text: "#ffffff"
},
fieldTranslations: {
nameTranslation: {
ar: "كروز أزول",
ru: "Круз Азул"
},
shortNameTranslation: { }
}
},
uniqueTournament: {
name: "Liga MX, Clausura",
slug: "liga-mx-clausura",
primaryColorHex: "#cd2c25",
secondaryColorHex: "#52b030",
category: {
name: "Mexico",
slug: "mexico",
sport: {
name: "Football",
slug: "football",
id: 1
},
id: 12,
flag: "mexico",
alpha2: "MX"
},
userCount: 34837,
id: 11620,
displayInverseHomeAwayTeams: false,
fieldTranslations: {
nameTranslation: {
ar: "الدوري المكسيكي، مرحلة الإياب",
hi: "लीगा एमएक्स, क्लॉसुरा",
bn: "লিগা এমএক্স , ক্লাউসুরা"
},
shortNameTranslation: { }
},
competitionType: "domestic-league"
},
season: {
name: "Primera Division, Clausura 2022",
year: "21/22",
editor: false,
id: 40080
}
},
{
statistics: {
accurateLongBalls: 3,
accurateLongBallsPercentage: 100,
accuratePasses: 45,
accuratePassesPercentage: 62.5,
aerialDuelsWon: 18,
assists: 0,
bigChancesCreated: 1,
bigChancesMissed: 2,
blockedShots: 0,
cleanSheet: 0,
dribbledPast: 4,
errorLeadToGoal: 0,
goals: 0,
goalsAssistsSum: 0,
goalsConceded: 3,
interceptions: 2,
keyPasses: 3,
minutesPlayed: 353,
passToAssist: 0,
rating: 6.7,
redCards: 0,
saves: 0,
shotsOnTarget: 1,
successfulDribbles: 2,
tackles: 10,
totalShots: 12,
yellowCards: 0,
totalRating: 40.2,
countRating: 6,
totalLongBalls: 3,
totalPasses: 72,
shotsFromInsideTheBox: 10,
appearances: 6,
type: "overall",
id: 0
},
year: "2022",
startYear: 2022,
endYear: 2022,
team: {
name: "Cruz Azul",
slug: "cruz-azul",
shortName: "Cruz Azul",
gender: "M",
sport: {
name: "Football",
slug: "football",
id: 1
},
userCount: 68602,
nameCode: "CAZ",
disabled: false,
national: false,
type: 0,
id: 1947,
teamColors: {
primary: "#0080c0",
secondary: "#ffffff",
text: "#ffffff"
},
fieldTranslations: {
nameTranslation: {
ar: "كروز أزول",
ru: "Круз Азул"
},
shortNameTranslation: { }
}
},
uniqueTournament: {
name: "CONCACAF Champions Cup",
slug: "concacaf-champions-cup",
primaryColorHex: "#333334",
secondaryColorHex: "#898a8a",
category: {
name: "North & Central America",
slug: "north-central-america",
sport: {
name: "Football",
slug: "football",
id: 1
},
id: 1469,
flag: "north-and-central-america"
},
userCount: 26480,
id: 498,
displayInverseHomeAwayTeams: false,
fieldTranslations: {
nameTranslation: {
ar: "كأس أبطال الكونكاكاف",
hi: "कोंकाकैफ चैंपियंस कप",
bn: "কনকাকাফ চ্যাম্পিয়ন্স কাপ"
},
shortNameTranslation: { }
},
competitionType: "international-cup"
},
season: {
name: "CONCACAF Champions League 2022",
year: "2022",
editor: false,
id: 40113
}
},
{
statistics: {
accurateCrosses: 3,
accurateCrossesPercentage: 50,
accurateLongBalls: 2,
accurateLongBallsPercentage: 66.67,
accuratePasses: 144,
accuratePassesPercentage: 72.36,
aerialDuelsWon: 20,
assists: 0,
bigChancesCreated: 1,
bigChancesMissed: 1,
blockedShots: 0,
cleanSheet: 0,
dribbledPast: 6,
errorLeadToGoal: 0,
goals: 4,
goalsAssistsSum: 4,
goalsConceded: 14,
interceptions: 5,
keyPasses: 5,
minutesPlayed: 933,
passToAssist: 0,
rating: 6.83,
redCards: 0,
saves: 0,
shotsOnTarget: 10,
successfulDribbles: 11,
tackles: 10,
totalShots: 29,
yellowCards: 3,
totalRating: 116.1,
countRating: 17,
totalLongBalls: 3,
totalCross: 6,
totalPasses: 199,
shotsFromInsideTheBox: 23,
appearances: 17,
type: "overall",
id: 0
},
year: "2021",
startYear: 2021,
endYear: 2021,
team: {
name: "Cruz Azul",
slug: "cruz-azul",
shortName: "Cruz Azul",
gender: "M",
sport: {
name: "Football",
slug: "football",
id: 1
},
userCount: 68602,
nameCode: "CAZ",
disabled: false,
national: false,
type: 0,
id: 1947,
teamColors: {
primary: "#0080c0",
secondary: "#ffffff",
text: "#ffffff"
},
fieldTranslations: {
nameTranslation: {
ar: "كروز أزول",
ru: "Круз Азул"
},
shortNameTranslation: { }
}
},
uniqueTournament: {
name: "Liga MX, Apertura",
slug: "liga-mx-apertura",
primaryColorHex: "#cd2c25",
secondaryColorHex: "#52b030",
category: {
name: "Mexico",
slug: "mexico",
sport: {
name: "Football",
slug: "football",
id: 1
},
id: 12,
flag: "mexico",
alpha2: "MX"
},
userCount: 39667,
id: 11621,
displayInverseHomeAwayTeams: false,
fieldTranslations: {
nameTranslation: {
ar: "دوري المكسيك، مرحلة الذهاب",
hi: "लीगा एमएक्स, एपर्टुरा",
bn: "লিগা এমএক্স, অ্যাপেরতুরা"
},
shortNameTranslation: { }
},
competitionType: "domestic-league"
},
season: {
name: "Primera Division, Apertura 2021",
year: "21/22",
editor: false,
id: 37238
}
},
{
statistics: {
accurateLongBalls: 3,
accurateLongBallsPercentage: 100,
accuratePasses: 46,
accuratePassesPercentage: 76.67,
aerialDuelsWon: 6,
assists: 3,
bigChancesCreated: 2,
bigChancesMissed: 2,
blockedShots: 1,
outfielderBlocks: 1,
cleanSheet: 2,
dribbledPast: 2,
errorLeadToGoal: 0,
goals: 0,
goalsAssistsSum: 3,
goalsConceded: 4,
interceptions: 3,
keyPasses: 4,
minutesPlayed: 305,
passToAssist: 0,
rating: 6.92,
redCards: 0,
saves: 0,
shotsOnTarget: 2,
successfulDribbles: 5,
tackles: 2,
totalShots: 6,
yellowCards: 1,
totalRating: 34.6,
countRating: 5,
totalLongBalls: 3,
totalPasses: 60,
shotsFromInsideTheBox: 4,
appearances: 5,
type: "overall",
id: 0
},
year: "2021",
startYear: 2021,
endYear: 2021,
team: {
name: "Cruz Azul",
slug: "cruz-azul",
shortName: "Cruz Azul",
gender: "M",
sport: {
name: "Football",
slug: "football",
id: 1
},
userCount: 68602,
nameCode: "CAZ",
disabled: false,
national: false,
type: 0,
id: 1947,
teamColors: {
primary: "#0080c0",
secondary: "#ffffff",
text: "#ffffff"
},
fieldTranslations: {
nameTranslation: {
ar: "كروز أزول",
ru: "Круз Азул"
},
shortNameTranslation: { }
}
},
uniqueTournament: {
name: "CONCACAF Champions Cup",
slug: "concacaf-champions-cup",
primaryColorHex: "#333334",
secondaryColorHex: "#898a8a",
category: {
name: "North & Central America",
slug: "north-central-america",
sport: {
name: "Football",
slug: "football",
id: 1
},
id: 1469,
flag: "north-and-central-america"
},
userCount: 26480,
id: 498,
displayInverseHomeAwayTeams: false,
fieldTranslations: {
nameTranslation: {
ar: "كأس أبطال الكونكاكاف",
hi: "कोंकाकैफ चैंपियंस कप",
bn: "কনকাকাফ চ্যাম্পিয়ন্স কাপ"
},
shortNameTranslation: { }
},
competitionType: "international-cup"
},
season: {
name: "CONCACAF Champions League 2021",
year: "2021",
editor: false,
id: 35618
}
},
{
statistics: {
accurateLongBalls: 1,
accurateLongBallsPercentage: 50,
accuratePasses: 6,
accuratePassesPercentage: 60,
aerialDuelsWon: 1,
assists: 1,
bigChancesCreated: 1,
bigChancesMissed: 0,
blockedShots: 0,
cleanSheet: 0,
dribbledPast: 0,
errorLeadToGoal: 0,
goals: 0,
goalsAssistsSum: 1,
goalsConceded: 1,
interceptions: 1,
keyPasses: 2,
minutesPlayed: 45,
passToAssist: 0,
rating: 7.4,
redCards: 0,
saves: 0,
shotsOnTarget: 1,
successfulDribbles: 0,
tackles: 3,
totalShots: 1,
yellowCards: 0,
totalRating: 7.4,
countRating: 1,
totalLongBalls: 2,
totalPasses: 10,
shotsFromInsideTheBox: 1,
appearances: 1,
type: "overall",
id: 0
},
year: "2021",
startYear: 2021,
endYear: 2021,
team: {
name: "Cruz Azul",
slug: "cruz-azul",
shortName: "Cruz Azul",
gender: "M",
sport: {
name: "Football",
slug: "football",
id: 1
},
userCount: 68602,
nameCode: "CAZ",
disabled: false,
national: false,
type: 0,
id: 1947,
teamColors: {
primary: "#0080c0",
secondary: "#ffffff",
text: "#ffffff"
},
fieldTranslations: {
nameTranslation: {
ar: "كروز أزول",
ru: "Круз Азул"
},
shortNameTranslation: { }
}
},
uniqueTournament: {
name: "Trofeo de Campeon de Campeones",
slug: "trofeo-de-campeon-de-campeones",
primaryColorHex: "#e2c038",
secondaryColorHex: "#aa8a2f",
category: {
name: "Mexico",
slug: "mexico",
sport: {
name: "Football",
slug: "football",
id: 1
},
id: 12,
flag: "mexico",
alpha2: "MX"
},
userCount: 1469,
id: 2103,
displayInverseHomeAwayTeams: false,
competitionType: "domestic-cup"
},
season: {
name: "Campeon de Campeones Liga MX 2021",
year: "2021",
editor: false,
id: 37022
}
},
{
statistics: {
accurateCrosses: 1,
accurateCrossesPercentage: 33.33,
accurateLongBalls: 2,
accurateLongBallsPercentage: 100,
accuratePasses: 79,
accuratePassesPercentage: 72.48,
aerialDuelsWon: 22,
assists: 1,
bigChancesCreated: 1,
bigChancesMissed: 1,
blockedShots: 0,
cleanSheet: 1,
dribbledPast: 4,
errorLeadToGoal: 0,
goals: 2,
goalsAssistsSum: 3,
goalsConceded: 6,
interceptions: 2,
keyPasses: 11,
minutesPlayed: 720,
passToAssist: 0,
rating: 6.75,
redCards: 0,
saves: 0,
shotsOnTarget: 7,
successfulDribbles: 12,
tackles: 9,
totalShots: 19,
yellowCards: 4,
totalRating: 108,
countRating: 16,
totalLongBalls: 2,
totalCross: 3,
totalPasses: 109,
shotsFromInsideTheBox: 16,
appearances: 18,
type: "overall",
id: 0
},
year: "2021",
startYear: 2021,
endYear: 2021,
team: {
name: "Cruz Azul",
slug: "cruz-azul",
shortName: "Cruz Azul",
gender: "M",
sport: {
name: "Football",
slug: "football",
id: 1
},
userCount: 68602,
nameCode: "CAZ",
disabled: false,
national: false,
type: 0,
id: 1947,
teamColors: {
primary: "#0080c0",
secondary: "#ffffff",
text: "#ffffff"
},
fieldTranslations: {
nameTranslation: {
ar: "كروز أزول",
ru: "Круз Азул"
},
shortNameTranslation: { }
}
},
uniqueTournament: {
name: "Liga MX, Clausura",
slug: "liga-mx-clausura",
primaryColorHex: "#cd2c25",
secondaryColorHex: "#52b030",
category: {
name: "Mexico",
slug: "mexico",
sport: {
name: "Football",
slug: "football",
id: 1
},
id: 12,
flag: "mexico",
alpha2: "MX"
},
userCount: 34837,
id: 11620,
displayInverseHomeAwayTeams: false,
fieldTranslations: {
nameTranslation: {
ar: "الدوري المكسيكي، مرحلة الإياب",
hi: "लीगा एमएक्स, क्लॉसुरा",
bn: "লিগা এমএক্স , ক্লাউসুরা"
},
shortNameTranslation: { }
},
competitionType: "domestic-league"
},
season: {
name: "Primera Division, Clausura 2021",
year: "20/21",
editor: false,
id: 35117
}
},
{
statistics: {
accuratePasses: 4,
accuratePassesPercentage: 57.14,
aerialDuelsWon: 2,
assists: 0,
bigChancesCreated: 0,
bigChancesMissed: 0,
cleanSheet: 0,
dribbledPast: 0,
errorLeadToGoal: 0,
goals: 0,
goalsAssistsSum: 0,
goalsConceded: 1,
interceptions: 1,
keyPasses: 1,
minutesPlayed: 51,
passToAssist: 0,
rating: 6.7,
redCards: 0,
saves: 0,
successfulDribbles: 1,
tackles: 0,
yellowCards: 0,
totalRating: 6.7,
countRating: 1,
totalPasses: 7,
shotsFromInsideTheBox: 0,
appearances: 1,
type: "overall",
id: 0
},
year: "2020",
startYear: 2020,
endYear: 2020,
team: {
name: "Cruz Azul",
slug: "cruz-azul",
shortName: "Cruz Azul",
gender: "M",
sport: {
name: "Football",
slug: "football",
id: 1
},
userCount: 68602,
nameCode: "CAZ",
disabled: false,
national: false,
type: 0,
id: 1947,
teamColors: {
primary: "#0080c0",
secondary: "#ffffff",
text: "#ffffff"
},
fieldTranslations: {
nameTranslation: {
ar: "كروز أزول",
ru: "Круз Азул"
},
shortNameTranslation: { }
}
},
uniqueTournament: {
name: "CONCACAF Champions Cup",
slug: "concacaf-champions-cup",
primaryColorHex: "#333334",
secondaryColorHex: "#898a8a",
category: {
name: "North & Central America",
slug: "north-central-america",
sport: {
name: "Football",
slug: "football",
id: 1
},
id: 1469,
flag: "north-and-central-america"
},
userCount: 26480,
id: 498,
displayInverseHomeAwayTeams: false,
fieldTranslations: {
nameTranslation: {
ar: "كأس أبطال الكونكاكاف",
hi: "कोंकाकैफ चैंपियंस कप",
bn: "কনকাকাফ চ্যাম্পিয়ন্স কাপ"
},
shortNameTranslation: { }
},
competitionType: "international-cup"
},
season: {
name: "CONCACAF Champions League 2020",
year: "2020",
editor: false,
id: 26749
}
},
{
statistics: {
accurateCrosses: 1,
accurateCrossesPercentage: 25,
accurateLongBalls: 3,
accurateLongBallsPercentage: 60,
accuratePasses: 127,
accuratePassesPercentage: 73.84,
aerialDuelsWon: 22,
assists: 3,
bigChancesCreated: 2,
bigChancesMissed: 7,
blockedShots: 1,
outfielderBlocks: 1,
cleanSheet: 0,
dribbledPast: 4,
errorLeadToGoal: 0,
goals: 4,
goalsAssistsSum: 7,
goalsConceded: 10,
interceptions: 1,
keyPasses: 11,
minutesPlayed: 889,
passToAssist: 0,
rating: 6.94,
redCards: 0,
saves: 0,
shotsOnTarget: 13,
successfulDribbles: 16,
tackles: 9,
totalShots: 36,
yellowCards: 1,
totalRating: 118,
countRating: 17,
totalLongBalls: 5,
totalCross: 4,
totalPasses: 172,
shotsFromInsideTheBox: 24,
appearances: 18,
type: "overall",
id: 0
},
year: "2020",
startYear: 2020,
endYear: 2020,
team: {
name: "Cruz Azul",
slug: "cruz-azul",
shortName: "Cruz Azul",
gender: "M",
sport: {
name: "Football",
slug: "football",
id: 1
},
userCount: 68602,
nameCode: "CAZ",
disabled: false,
national: false,
type: 0,
id: 1947,
teamColors: {
primary: "#0080c0",
secondary: "#ffffff",
text: "#ffffff"
},
fieldTranslations: {
nameTranslation: {
ar: "كروز أزول",
ru: "Круз Азул"
},
shortNameTranslation: { }
}
},
uniqueTournament: {
name: "Liga MX, Apertura",
slug: "liga-mx-apertura",
primaryColorHex: "#cd2c25",
secondaryColorHex: "#52b030",
category: {
name: "Mexico",
slug: "mexico",
sport: {
name: "Football",
slug: "football",
id: 1
},
id: 12,
flag: "mexico",
alpha2: "MX"
},
userCount: 39667,
id: 11621,
displayInverseHomeAwayTeams: false,
fieldTranslations: {
nameTranslation: {
ar: "دوري المكسيك، مرحلة الذهاب",
hi: "लीगा एमएक्स, एपर्टुरा",
bn: "লিগা এমএক্স, অ্যাপেরতুরা"
},
shortNameTranslation: { }
},
competitionType: "domestic-league"
},
season: {
name: "Primera Division, Apertura 2020",
year: "20/21",
editor: false,
id: 28233
}
},
{
statistics: {
accurateCrosses: 0,
accurateCrossesPercentage: 0,
accurateLongBalls: 5,
accurateLongBallsPercentage: 62.5,
accuratePasses: 68,
accuratePassesPercentage: 62.39,
aerialDuelsWon: 24,
assists: 1,
bigChancesCreated: 0,
bigChancesMissed: 1,
blockedShots: 0,
cleanSheet: 1,
dribbledPast: 3,
errorLeadToGoal: 0,
goals: 2,
goalsAssistsSum: 3,
goalsConceded: 9,
interceptions: 3,
keyPasses: 6,
minutesPlayed: 538,
passToAssist: 0,
rating: 6.79,
redCards: 0,
saves: 0,
shotsOnTarget: 5,
successfulDribbles: 7,
tackles: 3,
totalShots: 11,
yellowCards: 1,
totalRating: 61.1,
countRating: 9,
totalLongBalls: 8,
totalCross: 5,
totalPasses: 109,
shotsFromInsideTheBox: 7,
appearances: 9,
type: "overall",
id: 0
},
year: "2020",
startYear: 2020,
endYear: 2020,
team: {
name: "Cruz Azul",
slug: "cruz-azul",
shortName: "Cruz Azul",
gender: "M",
sport: {
name: "Football",
slug: "football",
id: 1
},
userCount: 68602,
nameCode: "CAZ",
disabled: false,
national: false,
type: 0,
id: 1947,
teamColors: {
primary: "#0080c0",
secondary: "#ffffff",
text: "#ffffff"
},
fieldTranslations: {
nameTranslation: {
ar: "كروز أزول",
ru: "Круз Азул"
},
shortNameTranslation: { }
}
},
uniqueTournament: {
name: "Liga MX, Clausura",
slug: "liga-mx-clausura",
primaryColorHex: "#cd2c25",
secondaryColorHex: "#52b030",
category: {
name: "Mexico",
slug: "mexico",
sport: {
name: "Football",
slug: "football",
id: 1
},
id: 12,
flag: "mexico",
alpha2: "MX"
},
userCount: 34837,
id: 11620,
displayInverseHomeAwayTeams: false,
fieldTranslations: {
nameTranslation: {
ar: "الدوري المكسيكي، مرحلة الإياب",
hi: "लीगा एमएक्स, क्लॉसुरा",
bn: "লিগা এমএক্স , ক্লাউসুরা"
},
shortNameTranslation: { }
},
competitionType: "domestic-league"
},
season: {
name: "Primera Division. Clausura 2020",
year: "19/20",
editor: false,
id: 26789
}
},
{
statistics: {
accurateCrosses: 0,
accurateCrossesPercentage: 0,
accurateLongBalls: 0,
accurateLongBallsPercentage: 0,
accuratePasses: 8,
accuratePassesPercentage: 61.54,
aerialDuelsWon: 2,
assists: 0,
bigChancesCreated: 0,
bigChancesMissed: 1,
blockedShots: 0,
cleanSheet: 0,
dribbledPast: 1,
errorLeadToGoal: 0,
goals: 0,
goalsAssistsSum: 0,
goalsConceded: 2,
interceptions: 0,
keyPasses: 0,
minutesPlayed: 97,
passToAssist: 0,
rating: 6.35,
redCards: 0,
saves: 0,
shotsOnTarget: 0,
successfulDribbles: 2,
tackles: 0,
totalShots: 2,
yellowCards: 1,
totalRating: 12.7,
countRating: 2,
totalLongBalls: 1,
totalCross: 2,
totalPasses: 13,
shotsFromInsideTheBox: 2,
appearances: 3,
type: "overall",
id: 0
},
year: "2019",
startYear: 2019,
endYear: 2019,
team: {
name: "Cruz Azul",
slug: "cruz-azul",
shortName: "Cruz Azul",
gender: "M",
sport: {
name: "Football",
slug: "football",
id: 1
},
userCount: 68602,
nameCode: "CAZ",
disabled: false,
national: false,
type: 0,
id: 1947,
teamColors: {
primary: "#0080c0",
secondary: "#ffffff",
text: "#ffffff"
},
fieldTranslations: {
nameTranslation: {
ar: "كروز أزول",
ru: "Круз Азул"
},
shortNameTranslation: { }
}
},
uniqueTournament: {
name: "Liga MX, Apertura",
slug: "liga-mx-apertura",
primaryColorHex: "#cd2c25",
secondaryColorHex: "#52b030",
category: {
name: "Mexico",
slug: "mexico",
sport: {
name: "Football",
slug: "football",
id: 1
},
id: 12,
flag: "mexico",
alpha2: "MX"
},
userCount: 39667,
id: 11621,
displayInverseHomeAwayTeams: false,
fieldTranslations: {
nameTranslation: {
ar: "دوري المكسيك، مرحلة الذهاب",
hi: "लीगा एमएक्स, एपर्टुरा",
bn: "লিগা এমএক্স, অ্যাপেরতুরা"
},
shortNameTranslation: { }
},
competitionType: "domestic-league"
},
season: {
name: "Primera Division, Apertura 2019",
year: "19/20",
editor: false,
id: 24002
}
}
],
typesMap: {
7: [
"overall",
"home",
"away"
],
23: [
"overall",
"home",
"away"
],
37: [
"overall",
"home",
"away"
],
133: [
"overall",
"home",
"away"
],
140: [
"overall",
"home",
"away"
],
328: [
"overall",
"home",
"away"
],
330: [
"overall",
"home",
"away"
],
340: [
"overall",
"home",
"away"
],
498: [
"overall",
"home",
"away"
],
679: [
"overall",
"home",
"away"
],
851: [
"overall",
"home",
"away"
],
853: [
"overall",
"home",
"away"
],
1794: [
"overall",
"away"
],
2103: [
"overall",
"away"
],
11620: [
"overall",
"home",
"away"
],
11621: [
"overall",
"home",
"away"
],
14100: [
"overall",
"home",
"away"
],
18872: [
"overall",
"away"
]
}
}