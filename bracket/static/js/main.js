$(document).ready(function () {

    var bracketMappingNextRound = {
        "L1": {"side": "L", "index": 5, "location": "home"},
        "L2": {"side": "L", "index": 5, "location": "away"},
        "L3": {"side": "L", "index": 6, "location": "home"},
        "L4": {"side": "L", "index": 6, "location": "away"},
        "L5": {"side": "L", "index": 7, "location": "home"},
        "L6": {"side": "L", "index": 7, "location": "away"},
        "L7": {"side": "M", "index": 1, "location": "home"},

        "R1": {"side": "R", "index": 5, "location": "home"},
        "R2": {"side": "R", "index": 5, "location": "away"},
        "R3": {"side": "R", "index": 6, "location": "home"},
        "R4": {"side": "R", "index": 6, "location": "away"},
        "R5": {"side": "R", "index": 7, "location": "home"},
        "R6": {"side": "R", "index": 7, "location": "away"},
        "R7": {"side": "M", "index": 1, "location": "away"}
    };

    $(".score-select").change(function () {
        var winner = (parseInt)($(this).val()) === 4;
        if (!winner) {
            return;
        }

        // TODO: check the other team has not '4' set as value.
        // TODO: hold the details so we can post it on save!

        var bracketSide = $(this).parent().data('bracketSide');
        var bracketIndex = $(this).parent().data('bracketIndex');
        var location = $(this).parent().data('location');

        var winningTeamDiv = getTeamCard(bracketSide, bracketIndex, location);
        var winningTeamScore = getTeamScore(bracketSide, bracketIndex, location);

        // Get the location of the next round and set the winning team's image.
        var nextRound = bracketMappingNextRound[bracketSide + bracketIndex];
        var cardTeamNextRound = getTeamCard(nextRound['side'], nextRound['index'], nextRound['location']);
        var img = $('<img src=' + winningTeamDiv.find('img:first').attr('src') + '>');
        cardTeamNextRound.html(img);

        var scoreTeamNextRound = getTeamScore(nextRound['side'], nextRound['index'], nextRound['location']);
        scoreTeamNextRound.find('span:first').html( winningTeamScore.find('span:first').html());
    });

    function getTeamCard(side, index, location) {
        return $(
            "div[data-bracket-side=" + side +
            "][data-location=" + location +
            "][data-bracket-index=" + index +
            "][class='card__team']");
    }

    function getTeamScore(side, index, location) {
        return $(
            "div[data-bracket-side=" + side +
            "][data-location=" + location +
            "][data-bracket-index=" + index +
            "][class='score__team']");
    }
});
