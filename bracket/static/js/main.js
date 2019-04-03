$(document).ready(function(){
  $(".score-select").change(function(){

      console.log($(this));
      console.log($(this).data());

      var bracketSide = $(this).data('bracketSide');
      var bracketIndex = $(this).data('bracketIndex');
      var score = $(this).val();

      if (score == 4) {


          // Set the image on the next round

            var cardTeamNextRound = $("div[data-bracket-index=" + 5 + "][class='card__team']");
            console.log(cardTeamNextRound);

            var img = $('<img id="dynamic">');
            img.attr('src', "/static/img/GSW.svg");

            cardTeamNextRound.html(img);

      }

      console.log(bracketSide, bracketIndex, $(this).val())

  });
});