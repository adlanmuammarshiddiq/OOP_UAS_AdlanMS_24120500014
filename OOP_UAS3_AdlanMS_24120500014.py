from datetime import date, time
from abc import ABC, abstractmethod


class Person(ABC):
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

    def getFullName(self) -> str:
        return f"{self.firstName} {self.lastName}"


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


class PersonCreator(ABC):
    @abstractmethod
    def createPerson(self, *args, **kwargs) -> Person:
        pass


class CoachCreator(PersonCreator):
    def createPerson(
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
    ) -> Coach:
        return Coach(
            personId,
            firstName,
            lastName,
            dateOfBirth,
            nationality,
            licenseLevel,
            coachId,
            teamId,
            role,
        )


class PlayerCreator(PersonCreator):
    def createPerson(
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
    ) -> Player:
        return Player(
            personId,
            firstName,
            lastName,
            dateOfBirth,
            nationality,
            jerseyNumber,
            marketValue,
            playerId,
            teamId,
            position,
            status,
        )


class StaffCreator(PersonCreator):
    def createPerson(
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
    ) -> Staff:
        return Staff(
            personId,
            firstName,
            lastName,
            dateOfBirth,
            nationality,
            department,
            staffId,
            clubId,
            role,
        )


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
        self.__sponsors = []
        self.__staff = []
        self.__contracts = []

    def manageBudget(self):
        pass

    def signSponsor(self, sponsor):
        self.__sponsors.append(sponsor)

    def getTeams(self):
        return self.__teams

    def addTeam(self, team):
        self.__teams.append(team)

    def addStaff(self, staff_member: Staff):
        self.__staff.append(staff_member)

    def addContract(self, contract):
        self.__contracts.append(contract)


class Team:
    def __init__(self, teamId: str, league: str, division: str, clubId: str, name: str):
        self.teamId = teamId
        self.league = league
        self.division = division
        self.clubId = clubId
        self.name = name
        self.__players = []
        self.__coaches = []
        self.__training_sessions = []

    def addPlayer(self, player: Player):
        if player not in self.__players:
            self.__players.append(player)

    def removePlayer(self, player: Player):
        if player in self.__players:
            self.__players.remove(player)

    def addCoach(self, coach: Coach):
        if coach not in self.__coaches:
            self.__coaches.append(coach)

    def scheduleTraining(self, session: "TrainingSession"):
        self.__training_sessions.append(session)


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
        self.__attendees = {}

    def recordAttendance(self, player: Player, present: bool):
        self.__attendees[player.personId] = present


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

    def generateReport(self) -> dict:
        return {
            "home_score": self.homeScore,
            "away_score": self.awayScore,
            "competition": self.competition,
        }


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

    def getMatches(self) -> list:
        return self.__matches

    def getStandings(self) -> dict:
        return {}


class Stadium:
    def __init__(self, stadiumId: str, name: str, capacity: int, address: str):
        self.stadiumId = stadiumId
        self.name = name
        self.capacity = capacity
        self.address = address

    def hostMatch(self, match: Match):
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
