echo -n "[*]Enter question link: ";read problem_link

echo "[*]Setting up...."


title_slug=$(echo $problem_link | cut -d / -f 5)

curl -s -X POST "https://leetcode.com/graphql/" \
    -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0" \
    -H "Content-Type: application/json" \
    -H "x-csrftoken: mpNhdKcqLtKNeACoVlEvbruIKG8oqMj6NmhNR3kqdYB2APZhRdHg3EOf5I1Yaheh" \
    -H "random-uuid: 05f7cf65-d1a4-b06f-0d38-eff257d28a3c" \
    -H "sentry-trace: eaf938c42e1b4d8ab0b9c317091d2529-952cfdee7e2e0827-0" \
    -H "baggage: sentry-environment=production,sentry-release=21ef4879,sentry-transaction=%2Fproblems%2F%5Bslug%5D%2F%5B%5B...tab%5D%5D,sentry-public_key=2a051f9838e2450fbdd5a77eb62cc83c,sentry-trace_id=eaf938c42e1b4d8ab0b9c317091d2529,sentry-sample_rate=0.03" \
    -H "Origin: https://leetcode.com" \
    -H "Connection: keep-alive" \
    --referer "https://leetcode.com/problems/$title_slug" \
    --data-raw '{"query":"query questionContent($titleSlug: String!) { question(titleSlug: $titleSlug) { content mysqlSchemas dataSchemas } }","variables":{"titleSlug":"'"$title_slug"'"},"operationName":"questionContent"}' > question.json

#clean_question=$(echo $raw_question | tr -d "[:cntrl:]")
#echo $raw_question | python3 -m json.tool
question=$(jq '.data.question.content' question.json | sed  -r 's/\\n+/\<br\>/g' | sed -r 's/(")</</g' | sed -r 's/>(")/>/g' | sed -r 's/\\r+//g')

mkdir -p $title_slug

echo "# Title: $title_slug" > $title_slug/readme.md
echo "## Question" >> $title_slug/readme.md
echo "$question">> $title_slug/readme.md
rm question.json
