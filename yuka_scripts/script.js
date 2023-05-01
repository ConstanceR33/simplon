

document.getElementById("button-api-test").addEventListener("click", function(){
  const codeBarre = document.getElementById("code-barres");
  fetch(`https://world.openfoodfacts.org/api/v0/product/${codeBarre.value}.json`)
    .then(response => response.json())
    .then(data => {
      const nutriScore = data.product.nutriscore_grade;
      const productName = data.product.product_name;
      const novaGroup = data.product.nova_group;
      const productCompo = data.product.ingredients_text;
      document.getElementById("nom-article").innerHTML = `${productName || 'Non renseigné'}`;
      document.getElementById("description").innerHTML = `<b>Ingrédients :</b> ${productCompo || 'Non renseignés'}`;
      document.getElementById("n-score").innerHTML = `<b>Score nutritionnel :</b> ${nutriScore.toUpperCase() || 'Non renseigné'}<br><br><b>Classification NOVA :</b> ${novaGroup || 'Non renseignée'}`;
    })
    .catch(error => console.error(error));
})
