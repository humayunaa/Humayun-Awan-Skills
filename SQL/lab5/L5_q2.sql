SELECT city.name AS city_name, city.population, country.name AS country_name, country.continent
FROM city, country
WHERE city.countrycode = country.code and city.population = (
    SELECT min(population)
    FROM city
);

#world
#2) Find the city with the lowest population and where it is located (country, region). Use a
#nested query