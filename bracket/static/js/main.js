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
        var matchUp = getMatchUp(bracketSide, bracketIndex);
        bracketUpdate[bracketSide + bracketIndex] = matchUp;

        var winningTeamLocation = null;
        if (matchUp.home.score === 4) {
            winningTeamLocation = 'home';
        } else if (matchUp.away.score === 4) {
            winningTeamLocation = 'away';
        }

        // Get the location of the next round and set the winning team's image.
        var nextRound = bracketMappingNextRound[bracketSide + bracketIndex];
        var cardTeamNextRound = getTeamCard(nextRound.side, nextRound.index, nextRound.location);
        var scoreTeamNextRound = getTeamScore(nextRound.side, nextRound.index, nextRound.location);

        if (winningTeamLocation === null || matchUp.home.score === matchUp.away.score) {
            cardTeamNextRound.html('<img src="/static/img/placeholder.svg" style="opacity: 0.3;"/>');
            scoreTeamNextRound.find('span:first').html('TBD');
            return;
        }

        var winningTeamDiv = getTeamCard(bracketSide, bracketIndex, winningTeamLocation);
        var winningTeamScore = getTeamScore(bracketSide, bracketIndex, winningTeamLocation);

        var img = '<img src=' + winningTeamDiv.find('img:first').attr('src') + '>';
        cardTeamNextRound.html(img);
        scoreTeamNextRound.find('span:first').html(winningTeamScore.find('span:first').html());
    });

    $(".save-button").click(function () {
        var data = JSON.stringify(bracketUpdate);
        console.log(bracketUpdate);
        console.log(data);
        $.ajax({
            type: 'POST',
            url: '/save-bracket',
            data: JSON.stringify(bracketUpdate),
            contentType:"application/json; charset=utf-8",
            dataType: 'json',
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            }
        }).done(function() {
            // location.reload();
            location.href = location.origin + location.pathname;
        });
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

    function getMatchUp(bracketSide, bracketIndex) {
        var homeTeamScoreDiv = getTeamScore(bracketSide, bracketIndex, 'home');
        var awayTeamScoreDiv = getTeamScore(bracketSide, bracketIndex, 'away');

        var homeTeamShort = $.trim(homeTeamScoreDiv.find('span:first').html());
        var awayTeamShort = $.trim(awayTeamScoreDiv.find('span:first').html());

        var homeTeamScore = parseInt(homeTeamScoreDiv.find('select:first').val());
        var awayTeamScore = parseInt(awayTeamScoreDiv.find('select:first').val());

        return {
            'home': {
                'team': homeTeamShort,
                'score': homeTeamScore
            },
            'away': {
                'team': awayTeamShort,
                'score': awayTeamScore
            }
        };
    }

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

});
