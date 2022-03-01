from django.contrib import admin

from core.models import Cashier, Vehicle, UseVehicle, Trip, Teasurer, Partner, MontlyPayment, President, \
                        Request, Demand, Justification, FinancialTransaction


admin.site.register(Cashier)
admin.site.register(Vehicle)
admin.site.register(UseVehicle)
admin.site.register(Trip)
admin.site.register(Teasurer)
admin.site.register(Demand)
admin.site.register(President)
admin.site.register(Partner)
admin.site.register(MontlyPayment)
admin.site.register(Request)
admin.site.register(Justification)
admin.site.register(FinancialTransaction)