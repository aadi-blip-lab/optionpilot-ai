"""
OptionPilot

Probability Engine

Version 1.0
"""


from dataclasses import dataclass


@dataclass
class Score:

    name: str

    points: int

    reason: str


class ProbabilityEngine:

    def __init__(self):

        self.items = []

    def add(self, name, points, reason):

        self.items.append(

            Score(
                name=name,
                points=points,
                reason=reason
            )

        )

    def total(self):

        return sum(x.points for x in self.items)

    def confidence(self):

        score = self.total()

        if score >= 90:
            return "VERY HIGH"

        if score >= 80:
            return "HIGH"

        if score >= 70:
            return "MEDIUM"

        return "LOW"

    def summary(self):

        return {

            "score": self.total(),

            "confidence": self.confidence(),

            "items": [

                {
                    "name": x.name,
                    "points": x.points,
                    "reason": x.reason
                }

                for x in self.items

            ]

        }
