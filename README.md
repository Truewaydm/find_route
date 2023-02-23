## Website for finding a route according to the given parameters.
### Exercise:
Finding a route to move from one point to another. The task is divided into 3 parts - settlements, trains, routes.

### Settlements.
Implement adding, editing, deleting a settlement, as well as page-by-page viewing of all available settlements. The locality has only a name

### Trains.
Implement adding, editing, deleting a train, as well as paging through all available trains. The train has a unique code (name), the beginning of the route, the end of the route and the travel time in conventional units. There can be several trains from one point to another, but they must differ in travel time.

### Routes.
The user selects the start and end point of the route, and also specifies the maximum travel time. Also, the user can add any number of intermediate cities through which the route should pass. Routes suitable for the conditions are loaded to it. Near each route there should be a button that allows you to save this route by giving it a name. When looking for routes, you need to pay attention to the direction of the train.

### Output results.
The output of routes is sorted by the shortest travel time. Those. the route with the shortest travel time is displayed first. The route description should contain information about where and where this route leads, travel time, and also contain a list of all trains that are on this route, indicating the train number, from where / where and travel time.
If the route is not found, display a message - "There is no route that satisfies the search conditions." If, however, the specified travel time is less than the minimum route time, then the message "The travel time is more than the one you selected. Change the time."

### Saved routes.
There should be a separate page with viewing routes. The route can only be saved, viewed and deleted. You cannot edit a saved route.

### Tests.
Should cover 40% of the code.

### Access to the site.
Access to adding/editing Trains/Cities, as well as deleting any records, should only be available to registered users.
