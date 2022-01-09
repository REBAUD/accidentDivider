# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 16:30:00 2022

@author: vincent.rebaud
"""
import os
import json
from company import Company

#
# # Key values for an enumerate
# class Key:
#     NAME = "name"
#     TYPE = "type"
#     VALUES = "values"


class Accident:

    # =============================================================================
    #     Handle a company definition
    # =============================================================================
    def __init__(self, verbose, inputDico):

        self.verbose = verbose
        self.global_percent = 0

        if "cost" in inputDico :
            self.global_cost = inputDico["cost"]
            self.reparted_cost = 0
        else :
            raise Exception('[Accident::Init] cost not found in input datas')

        if "companies" in inputDico :
            companies_list = []
            for company_input in inputDico["companies"] :
                company = Company(verbose, company_input, self.global_cost)
                self.global_percent += company.percent
                self.reparted_cost += company.cost
                companies_list.append(company)
        else :
            raise Exception('[Accident::Init] companies not found in input datas')
        self.companies_list = companies_list

        self.remaining_cost = self.global_cost- self.reparted_cost

        if verbose:
            print("Initial informations : ")
            print("Full cost {0:.2f} reparted in {1:.2f}%".format(self.global_cost, self.global_percent))
            if self.remaining_cost > 0 :
                print("So it remains {0:.2f} euros".format(self.remaining_cost))
            print("Company details : ")
            for company in self.companies_list :
                print("    - {0}".format(company))
            print("--------------------------------------------------------------\n\n")

        if self.remaining_cost > 0 :
            self.repartition()

    def repartition(self):

        iteration = 0
        stop = False

        while not stop:
            # Calculate sum of percent for companies with max reached
            percent_to_divide = 0
            for company in self.companies_list :
                if company.maxReached :
                    percent_to_divide += company.percent

            # Update the percent after distribution
            for company in self.companies_list:
                company.update_percent(percent_to_divide, self.global_percent)

            # Update the cost after distribution
            self.global_percent = 0
            self.reparted_cost = 0
            for company in self.companies_list:
                company.update_cost(self.remaining_cost)
                self.global_percent += company.percent
                self.reparted_cost += company.cost

            self.remaining_cost = self.global_cost - self.reparted_cost


            if self.verbose:
                print("Repartition {0} information : ".format(iteration + 1))
                print("Full cost {0:.2f} reparted in {1:.2f}%".format(self.global_cost, self.global_percent))
                if self.remaining_cost > 0:
                    print("So it remains {0:.2f} euros".format(self.remaining_cost))
                print("Company details : ")
                for company in self.companies_list:
                    print("    - {0}".format(company))
                print("--------------------------------------------------------------\n\n")

                # company.calculateCost()
                # print(company)

            iteration += 1
            stop = self.remaining_cost < 0.001 or iteration > 0 #len(self.companies_list)

        #
        #
        #     # print(iteration)
        #     iteration += 1




# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    inputDico = {}
    with open("inputFileFaucher.json", "r") as file :
        inputDico = json.load(file)

    accident = Accident(True, inputDico)
    # accident.repartition()

