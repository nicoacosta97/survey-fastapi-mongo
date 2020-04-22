
function sendDataToServer(survey) {
    var resultAsString = JSON.stringify(survey.data);
    $.ajax({
        url: "/",
        type: "POST",
        contentType: 'application/json',
        data: resultAsString,
        error: function (xhr, ajaxOptions, thrownError) {
            alert("Error al guardar los datos.", thrownError);
        }
    })
}

var survey = new Survey.Model(surveyJSON);

$("#surveyContainer").SurveyWindow({model: survey, onComplete: sendDataToServer});

