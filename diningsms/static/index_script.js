document.addEventListener('DOMContentLoaded', function() {
  const foodSearch = document.getElementById('food-search');
  const foodList = document.getElementById('food-list');
  fetch("/static/food_cattlet.json")
    .then(response => response.json())
    .then(data => {
      foodSearch.addEventListener('input', function () {
        const searchTerm = foodSearch.value.toLowerCase();
        foodList.innerHTML = '';
        const filteredFoods = data.filter(food => food.toLowerCase().includes(searchTerm)).slice(0, 10);
        filteredFoods.forEach((food, index) => {
          const foodItem = document.createElement('div');
          foodItem.classList.add('food-item');
          foodItem.innerHTML = `
            <input type="checkbox" id="food-${index}" name="food" value="${food}">
            <label for="food-${index}">${food}</label>
          `;
          foodList.appendChild(foodItem);
        });
      });
    });
});
