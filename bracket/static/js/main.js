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

    var bracketUpdate = {};

    $(".score-select").change(function () {
        var bracketSide = $(this).parent().data('bracketSide');
        var bracketIndex = $(this).parent().data('bracketIndex');

        var homeTeamScoreDiv = getTeamScore(bracketSide, bracketIndex, 'home');
        var awayTeamScoreDiv = getTeamScore(bracketSide, bracketIndex, 'away');

        var homeTeamShort = $.trim(homeTeamScoreDiv.find('span:first').html());
        var awayTeamShort = $.trim(awayTeamScoreDiv.find('span:first').html());

        var homeTeamScore = parseInt(homeTeamScoreDiv.find('select:first').val());
        var awayTeamScore = parseInt(awayTeamScoreDiv.find('select:first').val());

        bracketUpdate[bracketSide + bracketIndex] = {
            'home': {
                'team': homeTeamShort,
                'score': homeTeamScore
            },
            'away': {
                'team': awayTeamShort,
                'score': awayTeamScore
            }
        };

        console.log(bracketUpdate);


        var winningTeamLocation = null;
        if (homeTeamScore === 4) {
            winningTeamLocation = 'home';
        } else if (awayTeamScore === 4) {
            winningTeamLocation = 'away';
        }


        if (winningTeamLocation === null || homeTeamScore == awayTeamScore) {
            console.log('no winner');
            return;
        }




        var winningTeamDiv = getTeamCard(bracketSide, bracketIndex, winningTeamLocation);


        // Get the location of the next round and set the winning team's image.
        var nextRound = bracketMappingNextRound[bracketSide + bracketIndex];
        var cardTeamNextRound = getTeamCard(nextRound['side'], nextRound['index'], nextRound['location']);
        var img = $('<img src=' + winningTeamDiv.find('img:first').attr('src') + '>');
        cardTeamNextRound.html(img);

        var scoreTeamNextRound = getTeamScore(nextRound['side'], nextRound['index'], nextRound['location']);
        scoreTeamNextRound.find('span:first').html('bla');
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