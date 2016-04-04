=begin
This file is a convenience to use with mdl before committing. It currently matches the rules applied by Jenkins.
To use it run mdl in the root directory of the project, with the '-s' argument, as follows:

mdl -s md_style.rb README.md

(Where README.md is the file being tested)

The current rule set applied by Jenkins can be found at
https://github.com/NeCTAR-RC/nectar-ci/blob/master/builder-macros.yaml
in the builder named 'markdown-lint'

If this files passes whilst Jenkins fails, consider updating this file...
=end

all
exclude_tag :whitespace
exclude_tag :line_length
exclude_rule 'MD002' # First header should be a h1 header
exclude_rule 'MD006' # Lists at beginning of line
exclude_rule 'MD007' # List indentation
exclude_rule 'MD014' # Dollar signs used before commands without showing output
exclude_rule 'MD033' # Inline HTML
exclude_rule 'MD034' # Bare URL used
exclude_rule 'MD040' # Fenced code blocks should have a language specified
