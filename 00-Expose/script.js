var retards = []
let apiCallSncf = function (city) {
    let url = "https://api.sncf.com/v1/coverage/sncf/disruptions?from_datetime=20220916T000000&until%20=%7Bdatetime%7D&count=50&";
    var headers = new Headers({ "Authorization": "e938cc91-59c0-4214-ae07-f6f2352e6145" });
    
    // https://playground.navitia.io/play.html?request=https%3A%2F%2Fapi.sncf.com%2Fv1%2Fcoverage%2Fsncf%2Fdisruptions%3Fcount%1%26since%3D20220906T094820%26until%3D%257Bdatetime%257D%26

    fetch(url, { headers: headers })
        .then((response) =>
            response.json().then((data) => {

                console.log(data);
                for ( let element of data.disruptions ) {
                    if ( element.severity.effect === "SIGNIFICANT_DELAYS", element.status === "past" ) { retards.push(element) }
                }
                console.log(retards);
                for ( let element of retards ) {
                    document.body.innerHTML += '<p>Retard à ' + element.application_periods[0].end;
                }
            })
        )
        .catch((err) => {
            console.log("Erreur : " + err);
        }
    );
}

console.log(retards)