git checkout deploy
git merge --no-edit master
(cd app; npm install; bower install; grunt build --force)
git add app/dist
git commit -am "build"
git push heroku deploy:master
