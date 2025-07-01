function Notification({ avatarURL, message, time, unread }: Props): React.Node {
  return (
    <React.Fragment>
      {avatarURL && (
        <Avatar className="mr-3 align-self-center" imageURL={avatarURL} />
      )}
      <div>
        {message}
        {time && (
          <Text color="muted" size="small">
            {time}
          </Text>
        )}
      </div>
    </React.Fragment>
  );
}