# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 16:30:00 2022

@author: vincent.rebaud
"""
#
# # Key values for an enumerate
# class Key:
#     NAME = "name"
#     TYPE = "type"
#     VALUES = "values"


class Company:

    # =============================================================================
    #     Handle a company definition
    # =============================================================================
    def __init__(self, verbose, inputDico, global_cost):

        self.verbose = verbose
        self.maxReached = False
        self.cost = 0

        if "name" in inputDico :
            self.name = inputDico["name"]
        else :
            raise Exception('[Company::Init] name "{0}" not found in input datas')

        if "percent" in inputDico :
            self.percent = inputDico["percent"]
        else :
            raise Exception('[Company::Init] percent "{0}" not found in input datas')

        if "max_payment" in inputDico :
            self.max_payment = inputDico["max_payment"]
        else :
            self.max_payment = float("inf")

        self.update_cost(global_cost)

    def update_cost(self, global_cost):
        cost = self.cost + global_cost * self.percent / 100.0

        if cost >= self.max_payment :
            self.maxReached = True
            self.cost = self.max_payment
        else :
            self.maxReached = False
            self.cost = cost

    # =============================================================================
    #     Print callback function
    # =============================================================================
    def __str__(self):
        txt = "Company {0} : {1:.2f}% attribution, cost {3:.2f} euros, max {2:.2f} euros ({4})".format(self.name, self.percent, self.max_payment, self.cost, "Reached" if self.maxReached else "Not Reached")
        return txt

    def update_percent(self, remaining_percent):
        # print(remaining_percent)
        if self.maxReached:
            self.percent = 0
        else:
            # self.percent = self.percent * original_total / (original_total - percent_to_divide)
            self.percent = self.percent * 100 / remaining_percent

    def calculate_final_percent(self, global_cost, global_percent) :
        self.percent = self.cost * global_percent / global_cost





