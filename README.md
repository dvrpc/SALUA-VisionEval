# Vision-Eval-Input Files
azone_carsvc_characteristics.csv 

Link:https://github.com/VisionEval/VisionEval-Docs/blob/master/tutorials/verspm/Modules_and_Outputs.md/#createvehicletable

This file specifies the different characteristics for high and low car service level and is used in the CreateVehicleTable and AssignVehicleAge modules.

- Service level ?

# azone_charging_availability.csv

This file has data on proportion of different household types who has EV charging available and is used in the AssignHHVehiclePowertrain module.

azone_electricity_carbon_intensity.csv 

- ask Rob from Energy and CC 

This file is used to specify the carbon intensity of electricity and is optional (only needed if user wants to modify the values). 

The file is used in Initialize (VEPowertrainsAndFuels) and CalculateCarbonIntensity modules.

![image](https://user-images.githubusercontent.com/85887330/122805356-00c90200-d297-11eb-8e08-0f05a790ed3b.png)

https://github.com/VisionEval/VisionEval-Docs/blob/master/tutorials/verspm/Modules_and_Outputs.md/#assignhhvehiclepowertrain

# azone_fuel_power_cost.csv 

This file supplies data for retail cost of fuel and electricity and is used in the CalculateVehicleOperatingCost module.
- locate fuel retail costs
- ask Rob from Energy and CC 

https://github.com/VisionEval/VisionEval-Docs/blob/master/tutorials/verspm/Modules_and_Outputs.md/#calculatevehicleoperatingcost


# azone_gq_pop_by_age.csv

This file contains group quarters population estimates/forecasts by age and is used in the CreateHouseholds module.

- Refers to insitutional and non-institutions living quarters (dorms, nursing homes, correctional facilities,etc.)

- design a script that takes UrbanSim Output, aggregates geogrpahy to PUMA and has all the age ranges

https://github.com/VisionEval/VisionEval-Docs/blob/master/tutorials/verspm/Modules_and_Outputs.md/#createhouseholds

# azone_hh_pop_by_age.csv 

This file contains population estimates/forecasts by age and is used in the CreateHouseholds module.
- Census PUMS
- From UrbanSim Output

![image](https://user-images.githubusercontent.com/85887330/122803363-8303f700-d294-11eb-9262-049f60ae17ea.png)


# azone_hh_veh_mean_age.csv 

This file provides inputs for mean auto age and mean light truck age and is used in the AssignVehicleAge module.

![image](https://user-images.githubusercontent.com/85887330/122809238-d594e180-d29b-11eb-8e26-5cb0d587dce0.png)


# azone_hh_veh_own_taxes.csv 

This file provides inputs for flat fees/taxes (i.e. annual cost per vehicle) and ad valorem taxes (i.e. percentage of vehicle value paid in taxes). The file is used in CalculateVehicleOwnCost module.


https://github.com/VisionEval/VisionEval-Docs/blob/master/tutorials/verspm/Modules_and_Outputs.md/#calculatevehicleoperatingcost

# azone_hhsize_targets.csv 

This file contains the household specific targets and is used in CreateHouseholds module.

- Contact Person/Office who would have a good understadning of population forecasts by age group
- Age-based population forecasts are also included in UrbanSim outputs

![image](https://user-images.githubusercontent.com/85887330/122816533-de3de580-d2a4-11eb-89bf-79edc22f1776.png)


# azone_lttrk_prop.csv 

This file specifies the light truck proportion of the vehicle fleet and is used in AssignVehicleType module.

- Contact Rob from Energy & CC
- Contact DOT (see https://www.dmv.pa.gov/VEHICLE-SERVICES/Title-Registration/Pages/Fleet.aspx)

![image](https://user-images.githubusercontent.com/85887330/122815694-ca45b400-d2a3-11eb-9260-5898b704e29c.png)

https://github.com/VisionEval/VisionEval-Docs/blob/master/tutorials/verspm/Modules_and_Outputs.md/#assignvehicletype

# azone_payd_insurance_prop.csv 

This file provides inputs on the proportion of households having PAYD (pay-as-you-drive) insurance and is used in the CalculateVehicleOwnCost module.

* Not sure where to locate 

# azone_per_cap_inc.csv

This file contains information on regional average per capita household and group quarters income in year 2010 dollars and is used in the PredictIncome module.

![image](https://user-images.githubusercontent.com/85887330/122844662-2292ab00-d2d0-11eb-9693-09d6429f472f.png)

- Azone income per cap = total income of people in Azone/ # of Residents in A zone

# azone_prop_sov_dvmt_diverted.csv 

This file provides inputs for a goal for diverting a portion of SOV travel within a 20-mile tour distance and is used in the DivertSovTravel module.

- Doesnt need to be changed ?
- Contact whicever person/office would be able to provide a goal for SOV divertion

# azone_relative_employment.csv 

This file contains ratio of workers to persons by age and is used in the PredictWorkers module.
- Use UrbanSum Output

![image](https://user-images.githubusercontent.com/85887330/122814901-cf563380-d2a2-11eb-8c00-1a96b4991292.png)

https://github.com/VisionEval/VisionEval-Docs/blob/master/tutorials/verspm/Modules_and_Outputs.md/#predictworkers

# azone_veh_use_taxes.csv

This file supplies data for vehicle related taxes and is used in the CalculateVehicleOperatingCost module.
- Locate info in VRTs for A-zone using data from DOT 

![image](https://user-images.githubusercontent.com/85887330/122821773-40014e00-d2ab-11eb-9b30-e5369a5c5ae0.png)

https://github.com/VisionEval/VisionEval-Docs/blob/master/tutorials/verspm/Modules_and_Outputs.md/#calculatevehicleoperatingcost

# azone_vehicle_access_times.csv 

This file supplies data for vehicle access and egress time and is used in the CalculateVehicleOperatingCost module.

- Access refers to ?
- Egress: time is takes to exit vehicle

# bzone_transit_service.csv 

This file supplies the data on relative public transit accessibility and is used in the AssignTransitService module.

# bzone_carsvc_availability.csv 

This file contains the information about level of car service availability and is used in the AssignCarSvcAvailability module.

-Not sure where to find

# bzone_dwelling_units.csv

This file contains the number single-family, multi-family and group-quarter dwelling units and is used in the PredictHousing module.

- Can be found using Census Microdata 

![image](https://user-images.githubusercontent.com/85887330/122844004-b6637780-d2ce-11eb-91aa-9aa78a15695c.png)

https://github.com/VisionEval/VisionEval-Docs/blob/master/tutorials/verspm/Modules_and_Outputs.md/#predicthousing

# bzone_employment.csv 

This file contains the total, retail and service employment by zone and is used in the LocateEmployment module.

![image](https://user-images.githubusercontent.com/85887330/122843962-9e8bf380-d2ce-11eb-9e6c-623445c6971b.png)

- https://data.census.gov/cedsci/table?q=employment%20philadelphia&tid=ACSDP1Y2019.DP03&hidePreview=true 

https://github.com/VisionEval/VisionEval-Docs/blob/master/tutorials/verspm/Modules_and_Outputs.md/#locateemployment

# bzone_hh_inc_qrtl_prop.csv 

This file contains the proportion of households in 1st, 2nd, 3rd, and 4th quartile of household income and is used in the PredictHousing module.

![image](https://user-images.githubusercontent.com/85887330/122843708-1d346100-d2ce-11eb-939b-051ba1a01c86.png)

https://github.com/VisionEval/VisionEval-Docs/blob/master/tutorials/verspm/Modules_and_Outputs.md/#predicthousing 

- Average Incomes Table: https://data.census.gov/mdat/#/search?ds=ACSPUMS5Y2019&vv=*FINCP&wt=WGTP 

# bzone_lat_lon.csv 

This file contains the latitude and longitude of the centroid of the zone and is used in the LocateEmployment module.

- Find Centroid of DVRPC area ( , )

![image](https://user-images.githubusercontent.com/85887330/122843893-78665380-d2ce-11eb-930f-5127e908f2e2.png)

https://github.com/VisionEval/VisionEval-Docs/blob/master/tutorials/verspm/Modules_and_Outputs.md/#locateemployment

# bzone_network_design.csv 

This file contains the intersection density in terms of pedestrian-oriented intersections having four or more legs per square mile and is used in the Calculate4DMeasures module.

# bzone_parking.csv 

This file contains the parking information and is used in the AssignParkingRestrictions module.

# bzone_travel_demand_mgt.csv

This file contains the information about workers and households participating in demand management programs and is used in the AssignDemandManagement module.

# bzone_unprotected_area.csv

This file contains the information about unprotected (i.e., developable) area within the zone and is used in the Calculate4DMeasures module.

![image](https://user-images.githubusercontent.com/85887330/122823760-c028b300-d2ad-11eb-930a-5aebe317c93b.png)


# bzone_urban-mixed-use_prop.csv

This file contains the target proportion of households located in mixed-used neighborhoods in zone and is used in the CalculateUrbanMixMeasure module.

![image](https://user-images.githubusercontent.com/85887330/122823654-a1c2b780-d2ad-11eb-9e68-db7a49fa9777.png)


# bzone_urban-town_du_proportions.csv 

This file contains proportion of Single-Family, Multi-Family and Group Quarter dwelling units within the urban portion of the zone and is used in the AssignLocTypes module.

# marea_base_year_dvmt.csv 

- Use Units in Structure table to identify dwelling type proportions for Philadelphia County, PA in ACS
https://data.census.gov/cedsci/table?q=Philadelphia%20dwelling%20units&tid=ACSSE2019.K202504 

This file is used to specify to adjust the dvmt growth factors and is optional (only needed if user wants to modify the values). The file is used in the Initialize (VETravelPerformance), CalculateBaseRoadDvmt and CalculateFutureRoadDvmt modules.

# marea_congestion_charges.csv 

This file is used to specify the charges of vehicle travel for different congestion levels and is optional. The file is used in the Initialize (VETravelPerformance) and CalculateRoadPerformance modules.

# marea_dvmt_split_by_road_class.csv 

This file is used to specify the dvmt split for different road classes and is optional. The file is used in the Initialize (VETravelPerformance) and CalculateBaseRoadDvmt modules.

# marea_lane_miles.csv 

This file contains inputs on the numbers of freeway lane-miles and arterial lane-miles and is used in the AssignRoadMiles module.

# marea_operations_deployment.csv 

This file is used to specify the proportion of dvmt affected by operations for different road classes and is optional. The file is used in the Initialize (VETravelPerformance) and CalculateRoadPerformance modules.

# marea_speed_smooth_ecodrive.csv 

This input file supplies information of deployment of speed smoothing and ecodriving by road class and vehicle type and is used in the CalculateMpgMpkwhAdjustments module.

# marea_transit_ave_fuel_carbon_intensity.csv 

This file is used to specify the average carbon intensity of fuel used by transit and is optional. The file is used in the Initialize (VETravelPerformance) module.

# marea_transit_biofuel_mix.csv 

This file is used to specify the biofuel used by transit and is optional. The file is used in the Initialize (VETravelPerformance) and CalculateCarbonIntensity modules.

# marea_transit_fuel.csv

This file is used to specify the transit fuel proportions and is optional. The file is used in the Initialize (VETravelPerformance) and CalculateCarbonIntensity modules.

# marea_transit_powertrain_prop.csv 

This file is used to specify the mixes of transit vehicle powertrains and is optional. The file is used in the Initialize (VETravelPerformance) and CalculatePtranEnergyAndEmissions modules.

# marea_transit_service.csv

This file contains annual revenue-miles for different transit modes for metropolitan area and is used in the AssignTransitService module.

# other_ops_effectiveness.csv

This file is used to specify the delay effects of operations in different road classes and is optional (only needed if user wants to modify the values). The file is used in the Initialize (VETravelPerformance) and CalculateRoadPerformance modules.

# region_ave_fuel_carbon_intensity.csv 

This file is used to specify the average carbon density for different vehicle types and is optional (only needed if user wants to modify the values). The file is used in the Initialize (VETravelPerformance) and CalculateCarbonIntensity modules.

# region_base_year_hvytrk_dvmt.csv 

This file is used to specify the heavy truck dvmt for base year and is optional. The file is used in the Initialize (VETravelPerformance), CalculateBaseRoadDvmt and CalculateFutureRoadDvmt modules.

# region_carsvc_powertrain_prop.csv 

This file is used to specify the powertrain proportion of car services and is optional. The file is used in the Initialize (VETravelPerformance), AssignHhVehiclePowertrain and AdjustHhVehicleMpgMpkwh modules.

# region_comsvc_lttrk_prop.csv 

This file supplies data for the light truck proportion of commercial vehicles and is used in the CalculateComEnergyAndEmissions module.

# region_comsvc_powertrain_prop.csv 

This file is used to specify the powertrain proportion of commercial vehicles and is optional. The file is used in the Initialize (VEPowertrainsAndFuels) and CalculateComEnergyAndEmissions modules.

# region_hh_driver_adjust_prop.csv 

This file specifies the relative driver licensing rate relative to the model estimation data year and is used in the AssignDrivers module.

# region_hvytrk_powertrain_prop.csv

This file is used to specify the powertrain proportion of heavy duty trucks and is optional. The file is used in the Initialize 
(VEPowertrainsAndFuels) and CalculateComEnergyAndEmissions modules.

# region_prop_externalities_paid.csv 

This file supplies data for climate change and other social costs and is used in the CalculateVehicleOperatingCost module.

- What measures do we use to define the social costs?
