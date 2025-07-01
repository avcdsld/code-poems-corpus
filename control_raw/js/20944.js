function RuleSet(language) {
  var data = englishRuleSet;
  DEBUG && console.log(data);
  switch (language) {
    case 'EN':
      data = englishRuleSet;
      break;
    case 'DU':
      data = dutchRuleSet;
      break;
  }
  if (data.rules) {
    this.rules = {};
    var that = this;
    data.rules.forEach(function(ruleString) {
      that.addRule(TF_Parser.parse(ruleString));
    })
  }
  DEBUG && console.log(this.rules);
  DEBUG && console.log('Brill_POS_Tagger.read_transformation_rules: number of transformation rules read: ' + Object.keys(this.rules).length);
}