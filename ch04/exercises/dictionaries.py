Article = "We are already heading into Week 4 and last week was loaded with injuries. Below is a list of potentially available players to consider targeting in your league(s) to help fill the gaps.The waiver wire is a little slim this week for the wide receiver position, but there are a few options that are hopefully available for you. First, check to see if Treylon Burks or Romeo Doubs are on the wire. They are 76% and 40% rostered on Sleeper, so it’s likely they may already be taken Russell Gage is an option to consider while Julio Jones deals with the PCL injury. He saw some massive work against Green Bay in Week 3 when he caught 12 of his 13 targets for 87 yards and a touchdown. With Chris Godwin also battling injury, Tom Brady may be looking for him more often than not. He is 49% rostered on Sleeper.Out of some other names who may be available, Pittsburgh’s rookie wide receiver has the best schedule moving forward. There are already questions at quarterback after questionable play by Mitchell Trubisky, but Pickens is involved in that offense. He showed incredible athleticism with an acrobatic catch against the Browns and looks comfortable in his role.There are only a few things that are worse in fantasy than a litany of injuries to studs at running back. First and foremost, run… do not walk … to your waiver wire and check for Jamaal Williams, Khalil Herbert, and Alexander Mattison. If even one is available, smash that claim button or unload some serious FAAB. Williams and Herbert have already staked their claim in their respective offenses, regardless of the starters’ availability. With D’Andre Swift and David Montgomery expected to miss time, both of these running backs will see an increased workload on top of their already heavy usage.Mattison is in a slightly different position in Minnesota. However, with Dalvin Cook likely to miss time (and possibly stay that way all season with that separated shoulder) Mattison will see a massive amount in the Vikings’ offense."


substitutions = {
  "waiver wire":" scraps",
  "Jamaal Williams":"TD Thief",
  "Alexander Mattison":"Cook's handucffs",
  "rostered":"kept in jail",
  "injuries":"badges of weakness",
  "Pickens":"That dawg"
}

for key, value in substitutions.items():
 Article = Article.replace(key,value)


print(Article)