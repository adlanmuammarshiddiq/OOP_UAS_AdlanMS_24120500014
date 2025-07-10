from datetime import date, time


class Club:
    def __init__(
        self,
        clubId: str,
        name: str,
        foundingDate: date,
        budget: float,
        league: str,
        stadiumId: str,
    ):
        self.clubId = clubId
        self.name = name
        self.foundingDate = foundingDate
        self.budget = budget
        self.league = league
        self.stadiumId = stadiumId
        self.__teams = []

    def manageBudget(self):
        pass

    def signSponsor(self, sponsor):
        pass

    def getTeams(self):
        return self.__teams


class Person:
    def __init__(
        self,
        personId: str,
        firstName: str,
        lastName: str,
        dateOfBirth: date,
        nationality: str,
    ):
        self.personId = personId
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dateOfBirth
        self.nationality = nationality

    def getFullName(self):
        return f"{self.firstName} {self.lastName}"


class Team:
    def __init__(self, teamId: str, league: str, division: str, clubId: str, name: str):
        self.teamId = teamId
        self.league = league
        self.division = division
        self.clubId = clubId
        self.name = name
        self.__players = []
        self.__coaches = []

    def addPlayer(self, player):
        if player not in self.__players:
            self.__players.append(player)

    def removePlayer(self, player):
        if player in self.__players:
            self.__players.remove(player)

    def scheduleTraining(self, session):
        pass


class Sponsor:
    def __init__(
        self,
        sponsorId: str,
        name: str,
        contactPerson: str,
        phone: str,
        email: str,
        contractValue: float,
        contractStartDate: date,
        contractEndDate: date,
    ):
        self.sponsorId = sponsorId
        self.name = name
        self.contactPerson = contactPerson
        self.phone = phone
        self.email = email
        self.contractValue = contractValue
        self.contractStartDate = contractStartDate
        self.contractEndDate = contractEndDate

    def renewContract(self, newEndDate: date, newValue: float):
        self.contractEndDate = newEndDate
        self.contractValue = newValue


class Staff(Person):
    def __init__(
        self,
        personId: str,
        firstName: str,
        lastName: str,
        dateOfBirth: date,
        nationality: str,
        department: str,
        staffId: str,
        clubId: str,
        role: str,
    ):
        super().__init__(personId, firstName, lastName, dateOfBirth, nationality)
        self.department = department
        self.staffId = staffId
        self.clubId = clubId
        self.role = role

    def performDuties(self):
        pass


class Player(Person):
    def __init__(
        self,
        personId: str,
        firstName: str,
        lastName: str,
        dateOfBirth: date,
        nationality: str,
        jerseyNumber: int,
        marketValue: float,
        playerId: str,
        teamId: str,
        position: str,
        status: str,
    ):
        super().__init__(personId, firstName, lastName, dateOfBirth, nationality)
        self.jerseyNumber = jerseyNumber
        self.marketValue = marketValue
        self.playerId = playerId
        self.teamId = teamId
        self.position = position
        self.status = status

    def train(self):
        pass

    def playMatch(self):
        pass


class Coach(Person):
    def __init__(
        self,
        personId: str,
        firstName: str,
        lastName: str,
        dateOfBirth: date,
        nationality: str,
        licenseLevel: str,
        coachId: str,
        teamId: str,
        role: str,
    ):
        super().__init__(personId, firstName, lastName, dateOfBirth, nationality)
        self.licenseLevel = licenseLevel
        self.coachId = coachId
        self.teamId = teamId
        self.role = role

    def conductTraining(self):
        pass

    def selectSquad(self):
        pass


class TrainingSession:
    def __init__(
        self,
        sessionId: str,
        sessionDate: date,
        sessionTime: time,
        location: str,
        focusArea: str,
        teamId: str,
    ):
        self.sessionId = sessionId
        self.sessionDate = sessionDate
        self.sessionTime = sessionTime
        self.location = location
        self.focusArea = focusArea
        self.teamId = teamId

    def recordAttendance(self, player, present: bool):
        pass


class Match:
    def __init__(
        self,
        matchId: str,
        matchDate: date,
        matchTime: time,
        homeScore: int,
        awayScore: int,
        competition: str,
        homeTeamId: str,
        awayTeamId: str,
        stadiumId: str,
        seasonId: str,
    ):
        self.matchId = matchId
        self.matchDate = matchDate
        self.matchTime = matchTime
        self.homeScore = homeScore
        self.awayScore = awayScore
        self.competition = competition
        self.homeTeamId = homeTeamId
        self.awayTeamId = awayTeamId
        self.stadiumId = stadiumId
        self.seasonId = seasonId

    def recordScore(self, homeScore: int, awayScore: int):
        self.homeScore = homeScore
        self.awayScore = awayScore

    def generateReport(self):
        return {}


class Season:
    def __init__(
        self, seasonId: str, year: int, league: str, startDate: date, endDate: date
    ):
        self.seasonId = seasonId
        self.year = year
        self.league = league
        self.startDate = startDate
        self.endDate = endDate
        self.__matches = []

    def getMatches(self):
        return self.__matches

    def getStandings(self):
        return {}


class Stadium:
    def __init__(self, stadiumId: str, name: str, capacity: int, address: str):
        self.stadiumId = stadiumId
        self.name = name
        self.capacity = capacity
        self.address = address

    def hostMatch(self, match):
        pass


class Contract:
    def __init__(
        self,
        contractId: str,
        startDate: date,
        endDate: date,
        salary: float,
        clauses: str,
        clubId: str,
        personId: str,
    ):
        self.contractId = contractId
        self.startDate = startDate
        self.endDate = endDate
        self.salary = salary
        self.clauses = clauses
        self.clubId = clubId
        self.personId = personId

    def renew(self):
        pass

    def terminate(self):
        pass


# Pembuatan objek-objek sesuai dengan UML yang telah diberikan
stadium_cakrawala = Stadium(
    "STD001", "Stadion Cakrawala", 10000, "Jl. Universitas Cakrawala No. 1"
)
fc_cakrawala = Club(
    "CLUB001",
    "FC Cakrawala",
    date(2020, 1, 1),
    500000.00,
    "Liga Mahasiswa",
    stadium_cakrawala.stadiumId,
)

# Tim FC Cakrawala memiliki tim junior yang bernama FC Cakrawala Muda (U-23)
fc_cakrawala_muda = Team(
    "TEAM001", "Liga Mahasiswa", "U-23", fc_cakrawala.clubId, "FC Cakrawala Muda"
)

# Head Coach
coach_head_person = Person("PSN001", "Budi", "Santoso", date(1980, 5, 10), "Indonesia")
head_coach = Coach(
    coach_head_person.personId,
    coach_head_person.firstName,
    coach_head_person.lastName,
    coach_head_person.dateOfBirth,
    coach_head_person.nationality,
    "Pro License",
    "COACH001",
    fc_cakrawala_muda.teamId,
    "Head Coach",
)

# Assistant Coach
coach_assistant_person = Person(
    "PSN002", "Citra", "Dewi", date(1990, 8, 20), "Indonesia"
)
assistant_coach = Coach(
    coach_assistant_person.personId,
    coach_assistant_person.firstName,
    coach_assistant_person.lastName,
    coach_assistant_person.dateOfBirth,
    coach_assistant_person.nationality,
    "B License",
    "COACH002",
    fc_cakrawala_muda.teamId,
    "Assistant Coach",
)

# 15 mahasiswa Universitas Cakrawala Player utama.
players = []
for i in range(1, 16):
    player_person = Person(
        f"PSN{i+2:03d}", f"Pemain{i}", "Mahasiswa", date(2002, 1, i), "Indonesia"
    )
    player = Player(
        player_person.personId,
        player_person.firstName,
        player_person.lastName,
        player_person.dateOfBirth,
        player_person.nationality,
        i,
        10000.00,
        f"PLYR{i:02d}",
        fc_cakrawala_muda.teamId,
        "Midfielder",
        "Active",
    )
    players.append(player)

for player in players:
    fc_cakrawala_muda.addPlayer(player)

# Contract untuk Head Coach
contract_head_coach = Contract(
    "CTR001",
    date(2024, 7, 1),
    date(2025, 6, 30),
    5000000.00,
    "Klausul Pelatih Utama",
    fc_cakrawala.clubId,
    head_coach.personId,
)

# Contract untuk pemain muda (U-23)
contract_player1 = Contract(
    "CTR002",
    date(2024, 7, 1),
    date(2026, 6, 30),
    2000000.00,
    "Klausul Pemain Muda",
    fc_cakrawala.clubId,
    players[0].personId,
)
