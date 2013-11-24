git checkout deploy
git merge --no-edit master
(cd app; grunt build --force)
git add app/dist
git commit -am "build"
git push heroku deploy:master
